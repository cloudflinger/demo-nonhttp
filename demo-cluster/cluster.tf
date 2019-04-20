resource "digitalocean_kubernetes_cluster" "demo" {
  name    = "cloudflinger-demo"
  region  = "nyc1"
  version = "1.12.1-do.2"

  node_pool {
    name       = "woker-pool"
    size       = "s-2vcpu-2gb"
    node_count = 3
  }
}

resource "local_file" "kubeconfig" {
  content  = "${digitalocean_kubernetes_cluster.demo.kube_config.0.raw_config}"
  filename = "${path.module}/kubeconfig"

  lifecycle {
    # create_before_destroy = true
    ignore_changes = ["content"]
  }
}


# Getting Started

You'll need a kubernetes cluster and the ability to insert specs into the cluster. We use `kubectl` in this demo.

## Set up a demo DigitalOcean Cluster (Optional)

You'll have to have a digital ocean account an a personal access token.

```
cd demo-cluster/
terraform init
terraform apply -var do_token=${DIGITALOCEAN_TOKEN}
cd ../
```

## Update the manifests to use your namespace

```
$ sed -i 's|REPLACE_NAMESPACE|cloudflinger-demo|g' app.yml
$ sed -i 's|REPLACE_NAMESPACE|cloudflinger-demo|g' operator.yml
# On OSX use:
$ sed -i "" 's|REPLACE_NAMESPACE|cloudflinger-demo|g' app.yml
$ sed -i "" 's|REPLACE_NAMESPACE|cloudflinger-demo|g' operator.yml
```

## Customize app.yml (Optional)

This is where you specify port, command, etc.

## Apply the Manifests to your k8s cluster

```
kubectl apply -f operator.yml
kubectl apply -f app.yml
```

## Watch it work

```
kubectl -n cloudflinger-demo get pods
kubectl -n cloudflinger-demo logs pod nonhttp-app-<podsuffix> -f
kubectl -n cloudflinger-demo logs pod nonhttp-client-<podsuffix> -f
```


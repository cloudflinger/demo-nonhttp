# Getting Started

You'll need a kubernetes cluster and the ability to insert specs into the cluster. You can use either `helm` or `kubectl` in this demo.

## Set up a demo DigitalOcean Cluster (Optional)

You'll have to have a digital ocean account an a personal access token.

```
cd demo-cluster/
terraform init
terraform apply -var do_token=${DIGITALOCEAN_TOKEN}
cd ../
```

## Helm

This assumes you have helm installed locally and tiller installed in your cluster. You can learn more at the [helm homepage](https://helm.sh/) or [at the tiller rbac docs](https://github.com/helm/helm/blob/master/docs/rbac.md#tiller-and-role-based-access-control).

### Insert License Key

The chart is local to this repository. Run this command to update the license key

```
$ sed -i 's|REPLACE_LICENSE_KEY|GET_FROM_ACCOUNT|g' ./charts/cloudflinger-operator-demo/values.yaml
# On OSX use:
$ sed -i "" 's|REPLACE_LICENSE_KEY|GET_FROM_ACCOUNT|g' ./charts/cloudflinger-operator-demo/values.yaml
```

### Install Operator Release

```
helm install ./charts/cloudflinger-operator-demo/ --namespace cloudflinger-demo --name cloudflinger-operator-demo
```

### Install App Release

```
helm install ./charts/cloudflinger-app-demo/ --namespace cloudflinger-demo --name cloudflinger-app-demo
```

## Kubectl

Assumes you are going to use a namespace that doesn't exist called `cloudflinger-demo`. Feel free to change this. If you need to use an existing namespace, update operator.yml to not create a namespace.

### Update the manifests to use your namespace

```
$ sed -i 's|REPLACE_NAMESPACE|cloudflinger-demo|g' app.yml
$ sed -i 's|REPLACE_NAMESPACE|cloudflinger-demo|g' operator.yml
# On OSX use:
$ sed -i "" 's|REPLACE_NAMESPACE|cloudflinger-demo|g' app.yml
$ sed -i "" 's|REPLACE_NAMESPACE|cloudflinger-demo|g' operator.yml
```

### Customize app.yml / Insert License Key

This is where you specify port, command, etc.

You'll need to update the license key in order to authenticate for the demo.

```
$ sed -i 's|REPLACE_LICENSE_KEY|GET_FROM_ACCOUNT|g' app.yml
# On OSX use:
$ sed -i "" 's|REPLACE_LICENSE_KEY|GET_FROM_ACCOUNT|g' app.yml
```

### Apply the Manifests to your k8s cluster

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


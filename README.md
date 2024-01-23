# deploy-ml-model-as-dockerized-api-on-azure
Deploying a trained Machine Learning model as Dockerized API on Azure

**Steps to deploy:**
1. install azure cli
2. Install docker
2. create resource group and azure container registry
3. Build the code and dockerfile

4. terminal commands:
```
az login
```

```
sudo az acr login --name <AzureContainerRegistryName>
```

(check in access keys for username and password)

```
sudo docker images
```

```
sudo docker tag <ImageName> <AzureContainerRegistryName>.azurecr.io/<ImageName>
```

(server name in access keys page)

```
sudo docker images
```

```
sudo docker push <Azure Container Registry Name>.azurecr.io/<Image Name>
```

```
az container create --resource-group <ResourceGroupName> --name <ContainerName> --image <RegistryName>.azurecr.io/<your-image-name>:v1 --dns-name-label <DnsNameLabel> --ports 80
```

```
az container show --resource-group <ResourceGroupName> --name <ContainerName> --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
```


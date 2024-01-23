# deploy-ml-model-as-dockerized-api-on-azure

**Steps to deploy:**

1. **Build the Code and Dockerfile:** Prepare your application code and a Dockerfile, which is a text document that contains the commands to assemble the Docker image.
2. **Install Azure CLI:** Download and install the Azure Command Line Interface (CLI).
3. **Install Docker:** Download and install Docker, which is required to create and manage your application's image and container.
4. **Create Resource Group and Azure Container Registry (Azure Portal):** Set up a Resource Group in Azure for resource management and an Azure Container Registry (ACR) for storing and managing your private Docker container images.

**5. terminal commands:**

+ **Login to Azure:**

```
az login
```
Authenticate with Azure to access and manage Azure resources.

+ **Login to Azure Container Registry:**
```
sudo az acr login --name <AzureContainerRegistryName>
```
Use this command to authenticate with your Azure Container Registry. Check the "access keys" tab on ACR page


+ **List Docker Images:**

```
sudo docker images
```
This command lists all the Docker images available on your machine.

+ **Tag Docker Image for ACR:**

```
sudo docker tag <ImageName> <AzureContainerRegistryName>.azurecr.io/<ImageName>
```

Tag your Docker image for upload to Azure Container Registry.

+ **List Docker Images (Verification):**
```
sudo docker images
```
Verify the tagged Docker image.


+ **Push Docker Image to ACR:**
```
sudo docker push <Azure Container Registry Name>.azurecr.io/<Image Name>
```
Upload your Docker image to Azure Container Registry.


+ **Create Azure Container Instance:**
```
az container create --resource-group <ResourceGroupName> --name <ContainerName> --image <RegistryName>.azurecr.io/<your-image-name>:v1 --dns-name-label <DnsNameLabel> --ports 80
```
Deploy your containerized application on Azure Container Instance.

+ **Check Container Deployment Status:**

```
az container show --resource-group <ResourceGroupName> --name <ContainerName> --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" --out table
```
Check the deployment status and obtain the Fully Qualified Domain Name (FQDN) of your deployed container.

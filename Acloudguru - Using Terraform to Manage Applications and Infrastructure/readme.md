# Basic commands
terreform version
terraform -chdir=<path_to/tf> <subcommand> # Switch to working directory
terraform init
terraform plan
    terraform plan -out <plan_name> # output a deployment plan
    terraform plan -destroy # output a destroy plan
terraform apply
    terraform apply <plan_name> # apply a specific plan
    terraform apply -var my_variable=<variable> #Pass a variable via the command line
terraform destroy
terraform providers # Get provider info used in configuration

### Example block
resource "aws_vpc" "main" {
    cidr_block = var.base_cidr_block
}

<BLOCK TYPE> "<BLOCK LABEL>" "<BLOCK LABEL>" {
    #Block Body
    <IDENTIFIER> = <EXPRESSION> #Argument (Assigne a value to a name)
    #Expression respresent a value
}

### File extension
.tf
.tf.json

### Text encodeing
UTF-8

# Directories and Modeules
Modeuls are a collection of .tf and or .tf.json files kept together in a directory. A module consistes of only the top-level config files in the directory. A nested directory is treated as a seperate module and may not be automatically included. 

### Root Module
Terraform configuration consistes of a root module and a few child modules. The root module is the working directory where Terraform is invoked.

### Resources
Resources are the most important part of the Terraform language. Resource blocks describe infrustructure objects like virtual networks, computer instance, or components like DNS records.

#### Resource Types:
- Providers
- Arguments
- Documentation

### Meta Arguments
depends_on
count
for_each
provider
lifecycle
provisioner and connection

### Operation Timeout
There are some resource types that provide special timeouts, nested block arguments that allow for customization of how long certain operations are allowed to take before they are deemed failed.

### How configuration is applied
- Create
- Destroy
- Update in-place
- Destroy and re-create

### Input Variables
The name of a variable can be any valid identifier except for source, version, providers, count, for_each, lifecycle, depends_on and locals
These are reserved KWs

#### Optional Arguments for variable
default (makes the variable optional)
type (acceptable type)
description (input variable doc)
validation (validation rules in addition to type constraints)
sensetive (Limits the terraform UI output)

#### Type Constraints
string
number
bool

#### Type Constructors
list(<type>)
set(<type>)
map(<type>)
object({<attribute> = <type>, ...})
tuple([<type>, ...])

Value can be accessed from an expression, such as var.<var_name>.

a value assigned to a variable can only be accessed in an expression within the module it was declared

input_variable_order
![Input Variable order](input_variable_order.png "Input Variable")

### Output Variabls
- A child module can use them to expose a subset of resource attributes to the parent module.
- A root module can use them to print values in the CLI
- Root module outputs can be accessed by other configurations via the terraform_remote_state data source

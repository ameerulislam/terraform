#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here


app = App()
stack = MyStack(app, "youtubecdkdemo")
CloudBackend(stack,
  hostname='app.terraform.io',
  organization='organicsolutions',
  workspaces=NamedCloudWorkspace('youtubecdkdemo')
)

app.synth()

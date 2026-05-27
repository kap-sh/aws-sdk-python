"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceType``."""

from typing import Literal, TypeAlias

NetworkInterfaceType: TypeAlias = Literal[
    "interface",
    "natGateway",
    "efa",
    "efa-only",
    "trunk",
    "load_balancer",
    "network_load_balancer",
    "vpc_endpoint",
    "branch",
    "transit_gateway",
    "lambda",
    "quicksight",
    "global_accelerator_managed",
    "api_gateway_managed",
    "gateway_load_balancer",
    "gateway_load_balancer_endpoint",
    "iot_rules_managed",
    "aws_codestar_connections_managed",
]

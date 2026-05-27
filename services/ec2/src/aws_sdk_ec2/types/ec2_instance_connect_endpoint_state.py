"""Generated from Smithy shape ``com.amazonaws.ec2#Ec2InstanceConnectEndpointState``."""

from typing import Literal, TypeAlias

Ec2InstanceConnectEndpointState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
    "update-in-progress",
    "update-complete",
    "update-failed",
]

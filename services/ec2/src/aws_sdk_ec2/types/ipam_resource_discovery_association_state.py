"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoveryAssociationState``."""

from typing import Literal, TypeAlias

IpamResourceDiscoveryAssociationState: TypeAlias = Literal[
    "associate-in-progress",
    "associate-complete",
    "associate-failed",
    "disassociate-in-progress",
    "disassociate-complete",
    "disassociate-failed",
    "isolate-in-progress",
    "isolate-complete",
    "restore-in-progress",
]

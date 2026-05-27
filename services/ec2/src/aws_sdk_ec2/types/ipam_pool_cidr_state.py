"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrState``."""

from typing import Literal, TypeAlias

IpamPoolCidrState: TypeAlias = Literal[
    "pending-provision",
    "provisioned",
    "failed-provision",
    "pending-deprovision",
    "deprovisioned",
    "failed-deprovision",
    "pending-import",
    "failed-import",
]

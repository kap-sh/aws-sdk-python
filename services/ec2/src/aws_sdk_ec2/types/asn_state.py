"""Generated from Smithy shape ``com.amazonaws.ec2#AsnState``."""

from typing import Literal, TypeAlias

AsnState: TypeAlias = Literal[
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-deprovision",
    "pending-provision",
    "provisioned",
]

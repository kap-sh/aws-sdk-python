"""Generated from Smithy shape ``com.amazonaws.ec2#ByoipCidrState``."""

from typing import Literal, TypeAlias

ByoipCidrState: TypeAlias = Literal[
    "advertised",
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-advertising",
    "pending-deprovision",
    "pending-provision",
    "pending-withdrawal",
    "provisioned",
    "provisioned-not-publicly-advertisable",
]

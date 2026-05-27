"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationTokenState``."""

from typing import Literal, TypeAlias

IpamExternalResourceVerificationTokenState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
]

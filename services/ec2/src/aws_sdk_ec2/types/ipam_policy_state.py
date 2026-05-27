"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyState``."""

from typing import Literal, TypeAlias

IpamPolicyState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
    "isolate-in-progress",
    "isolate-complete",
    "restore-in-progress",
]

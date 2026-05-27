"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverTargetState``."""

from typing import Literal, TypeAlias

IpamPrefixListResolverTargetState: TypeAlias = Literal[
    "create-in-progress",
    "create-complete",
    "create-failed",
    "modify-in-progress",
    "modify-complete",
    "modify-failed",
    "sync-in-progress",
    "sync-complete",
    "sync-failed",
    "delete-in-progress",
    "delete-complete",
    "delete-failed",
    "isolate-in-progress",
    "isolate-complete",
    "restore-in-progress",
]

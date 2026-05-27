"""Generated from Smithy shape ``com.amazonaws.ec2#FleetStateCode``."""

from typing import Literal, TypeAlias

FleetStateCode: TypeAlias = Literal[
    "submitted",
    "active",
    "deleted",
    "failed",
    "deleted_running",
    "deleted_terminating",
    "modifying",
]

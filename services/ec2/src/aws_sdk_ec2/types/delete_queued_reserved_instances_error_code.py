"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteQueuedReservedInstancesErrorCode``."""

from typing import Literal, TypeAlias

DeleteQueuedReservedInstancesErrorCode: TypeAlias = Literal[
    "reserved-instances-id-invalid",
    "reserved-instances-not-in-queued-state",
    "unexpected-error",
]

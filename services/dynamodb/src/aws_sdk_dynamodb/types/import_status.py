"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportStatus``."""

from typing import Literal, TypeAlias

ImportStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "CANCELLING",
    "CANCELLED",
    "FAILED",
]

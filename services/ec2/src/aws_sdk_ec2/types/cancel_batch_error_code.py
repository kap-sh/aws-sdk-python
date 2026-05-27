"""Generated from Smithy shape ``com.amazonaws.ec2#CancelBatchErrorCode``."""

from typing import Literal, TypeAlias

CancelBatchErrorCode: TypeAlias = Literal[
    "fleetRequestIdDoesNotExist",
    "fleetRequestIdMalformed",
    "fleetRequestNotInCancellableState",
    "unexpectedError",
]

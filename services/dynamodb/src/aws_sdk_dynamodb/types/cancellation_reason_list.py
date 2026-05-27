"""Generated from Smithy shape ``com.amazonaws.dynamodb#CancellationReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.cancellation_reason

CancellationReasonList: TypeAlias = list[
    "aws_sdk_dynamodb.types.cancellation_reason.CancellationReason"
]

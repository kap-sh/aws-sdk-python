"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.throttling_reason

ThrottlingReasonList: TypeAlias = list[
    "aws_sdk_dynamodb.types.throttling_reason.ThrottlingReason"
]

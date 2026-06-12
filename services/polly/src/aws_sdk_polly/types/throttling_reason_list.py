"""Generated from Smithy shape ``com.amazonaws.polly#ThrottlingReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_polly.types.throttling_reason

ThrottlingReasonList: TypeAlias = list[
    "aws_sdk_polly.types.throttling_reason.ThrottlingReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingReasonList) -> list:
    import aws_sdk_polly.types.throttling_reason

    out: list = []
    for item in value:
        out.append(aws_sdk_polly.types.throttling_reason.serialize_json(item))
    return out


def deserialize_json(data: list) -> ThrottlingReasonList:
    import aws_sdk_polly.types.throttling_reason

    out: ThrottlingReasonList = []
    for item in data:
        out.append(aws_sdk_polly.types.throttling_reason.deserialize_json(item))
    return out

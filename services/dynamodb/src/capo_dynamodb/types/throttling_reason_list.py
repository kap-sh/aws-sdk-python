"""Generated from Smithy shape ``com.amazonaws.dynamodb#ThrottlingReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.throttling_reason

ThrottlingReasonList: TypeAlias = list[
    "capo_dynamodb.types.throttling_reason.ThrottlingReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ThrottlingReasonList) -> list:
    import capo_dynamodb.types.throttling_reason

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.throttling_reason.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ThrottlingReasonList:
    import capo_dynamodb.types.throttling_reason

    out: ThrottlingReasonList = []
    for item in data:
        out.append(capo_dynamodb.types.throttling_reason.deserialize_aws_json_1_0(item))
    return out

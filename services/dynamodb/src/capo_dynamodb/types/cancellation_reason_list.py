"""Generated from Smithy shape ``com.amazonaws.dynamodb#CancellationReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.cancellation_reason

CancellationReasonList: TypeAlias = list[
    "capo_dynamodb.types.cancellation_reason.CancellationReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancellationReasonList) -> list:
    import capo_dynamodb.types.cancellation_reason

    out: list = []
    for item in value:
        out.append(capo_dynamodb.types.cancellation_reason.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CancellationReasonList:
    import capo_dynamodb.types.cancellation_reason

    out: CancellationReasonList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_dynamodb.types.cancellation_reason.deserialize_aws_json_1_0(item)
        )
    return out

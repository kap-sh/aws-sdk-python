"""Generated from Smithy shape ``com.amazonaws.acm#ThrottlingReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.throttling_reason

ThrottlingReasonList: TypeAlias = list[
    "capo_acm.types.throttling_reason.ThrottlingReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThrottlingReasonList) -> list:
    import capo_acm.types.throttling_reason

    out: list = []
    for item in value:
        out.append(capo_acm.types.throttling_reason.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThrottlingReasonList:
    import capo_acm.types.throttling_reason

    out: ThrottlingReasonList = []
    for item in data:
        out.append(capo_acm.types.throttling_reason.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#StatusReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.status_reason_code

StatusReasonCodes: TypeAlias = list[
    "capo_partnercentral_benefits.types.status_reason_code.StatusReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatusReasonCodes) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> StatusReasonCodes:
    return list(data)

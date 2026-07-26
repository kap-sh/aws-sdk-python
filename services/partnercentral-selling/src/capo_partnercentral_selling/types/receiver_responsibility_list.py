"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReceiverResponsibilityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.receiver_responsibility

ReceiverResponsibilityList: TypeAlias = list[
    "capo_partnercentral_selling.types.receiver_responsibility.ReceiverResponsibility"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiverResponsibilityList) -> list:
    import capo_partnercentral_selling.types.receiver_responsibility

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.receiver_responsibility.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ReceiverResponsibilityList:
    import capo_partnercentral_selling.types.receiver_responsibility

    out: ReceiverResponsibilityList = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.receiver_responsibility.deserialize_aws_json_1_0(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SenderContactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.sender_contact

SenderContactList: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.sender_contact.SenderContact"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SenderContactList) -> list:
    import aws_sdk_partnercentral_selling.types.sender_contact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.sender_contact.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SenderContactList:
    import aws_sdk_partnercentral_selling.types.sender_contact

    out: SenderContactList = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.sender_contact.deserialize_aws_json_1_0(
                item
            )
        )
    return out

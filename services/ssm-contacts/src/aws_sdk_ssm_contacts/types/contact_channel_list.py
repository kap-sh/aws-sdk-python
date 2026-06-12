"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact_channel

ContactChannelList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.contact_channel.ContactChannel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactChannelList) -> list:
    import aws_sdk_ssm_contacts.types.contact_channel

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.contact_channel.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContactChannelList:
    import aws_sdk_ssm_contacts.types.contact_channel

    out: ContactChannelList = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.contact_channel.deserialize_aws_json_1_1(item)
        )
    return out

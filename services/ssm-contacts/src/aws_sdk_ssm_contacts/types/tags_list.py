"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.tag

TagsList: TypeAlias = list["aws_sdk_ssm_contacts.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsList) -> list:
    import aws_sdk_ssm_contacts.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagsList:
    import aws_sdk_ssm_contacts.types.tag

    out: TagsList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.tag.deserialize_aws_json_1_1(item))
    return out

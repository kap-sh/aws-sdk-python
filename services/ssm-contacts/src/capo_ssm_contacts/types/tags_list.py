"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.tag

TagsList: TypeAlias = list["capo_ssm_contacts.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagsList) -> list:
    import capo_ssm_contacts.types.tag

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagsList:
    import capo_ssm_contacts.types.tag

    out: TagsList = []
    for item in data:
        out.append(capo_ssm_contacts.types.tag.deserialize_aws_json_1_1(item))
    return out

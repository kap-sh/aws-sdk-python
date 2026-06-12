"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ResolutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.resolution_contact

ResolutionList: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.resolution_contact.ResolutionContact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolutionList) -> list:
    import aws_sdk_ssm_contacts.types.resolution_contact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.resolution_contact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolutionList:
    import aws_sdk_ssm_contacts.types.resolution_contact

    out: ResolutionList = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.resolution_contact.deserialize_aws_json_1_1(item)
        )
    return out

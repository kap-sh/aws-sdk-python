"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#TargetsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.target

TargetsList: TypeAlias = list["aws_sdk_ssm_contacts.types.target.Target"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetsList) -> list:
    import aws_sdk_ssm_contacts.types.target

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.target.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TargetsList:
    import aws_sdk_ssm_contacts.types.target

    out: TargetsList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.target.deserialize_aws_json_1_1(item))
    return out

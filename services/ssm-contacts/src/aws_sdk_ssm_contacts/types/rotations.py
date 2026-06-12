"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Rotations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.rotation

Rotations: TypeAlias = list["aws_sdk_ssm_contacts.types.rotation.Rotation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rotations) -> list:
    import aws_sdk_ssm_contacts.types.rotation

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.rotation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Rotations:
    import aws_sdk_ssm_contacts.types.rotation

    out: Rotations = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.rotation.deserialize_aws_json_1_1(item))
    return out

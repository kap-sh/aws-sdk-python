"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Rotations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_contacts.types.rotation

Rotations: TypeAlias = list["capo_ssm_contacts.types.rotation.Rotation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rotations) -> list:
    import capo_ssm_contacts.types.rotation

    out: list = []
    for item in value:
        out.append(capo_ssm_contacts.types.rotation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Rotations:
    import capo_ssm_contacts.types.rotation

    out: Rotations = []
    for item in data:
        out.append(capo_ssm_contacts.types.rotation.deserialize_aws_json_1_1(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.rotation_override

RotationOverrides: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.rotation_override.RotationOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationOverrides) -> list:
    import aws_sdk_ssm_contacts.types.rotation_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.rotation_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RotationOverrides:
    import aws_sdk_ssm_contacts.types.rotation_override

    out: RotationOverrides = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.rotation_override.deserialize_aws_json_1_1(item)
        )
    return out

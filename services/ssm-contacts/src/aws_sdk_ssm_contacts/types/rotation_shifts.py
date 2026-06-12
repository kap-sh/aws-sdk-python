"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RotationShifts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.rotation_shift

RotationShifts: TypeAlias = list[
    "aws_sdk_ssm_contacts.types.rotation_shift.RotationShift"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationShifts) -> list:
    import aws_sdk_ssm_contacts.types.rotation_shift

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_contacts.types.rotation_shift.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RotationShifts:
    import aws_sdk_ssm_contacts.types.rotation_shift

    out: RotationShifts = []
    for item in data:
        out.append(
            aws_sdk_ssm_contacts.types.rotation_shift.deserialize_aws_json_1_1(item)
        )
    return out

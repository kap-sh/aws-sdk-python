"""Generated from Smithy shape ``com.amazonaws.kms#RotationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.rotations_list_entry

RotationsList: TypeAlias = list[
    "aws_sdk_kms.types.rotations_list_entry.RotationsListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotationsList) -> list:
    import aws_sdk_kms.types.rotations_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.rotations_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RotationsList:
    import aws_sdk_kms.types.rotations_list_entry

    out: RotationsList = []
    for item in data:
        out.append(
            aws_sdk_kms.types.rotations_list_entry.deserialize_aws_json_1_1(item)
        )
    return out

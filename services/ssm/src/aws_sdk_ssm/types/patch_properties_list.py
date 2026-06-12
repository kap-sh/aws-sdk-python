"""Generated from Smithy shape ``com.amazonaws.ssm#PatchPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.patch_property_entry

PatchPropertiesList: TypeAlias = list[
    "aws_sdk_ssm.types.patch_property_entry.PatchPropertyEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchPropertiesList) -> list:
    import aws_sdk_ssm.types.patch_property_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.patch_property_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PatchPropertiesList:
    import aws_sdk_ssm.types.patch_property_entry

    out: PatchPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.patch_property_entry.deserialize_aws_json_1_1(item)
        )
    return out

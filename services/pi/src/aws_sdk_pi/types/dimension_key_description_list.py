"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_key_description

DimensionKeyDescriptionList: TypeAlias = list[
    "aws_sdk_pi.types.dimension_key_description.DimensionKeyDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDescriptionList) -> list:
    import aws_sdk_pi.types.dimension_key_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pi.types.dimension_key_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionKeyDescriptionList:
    import aws_sdk_pi.types.dimension_key_description

    out: DimensionKeyDescriptionList = []
    for item in data:
        out.append(
            aws_sdk_pi.types.dimension_key_description.deserialize_aws_json_1_1(item)
        )
    return out

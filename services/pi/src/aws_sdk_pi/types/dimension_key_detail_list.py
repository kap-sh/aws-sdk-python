"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_key_detail

DimensionKeyDetailList: TypeAlias = list[
    "aws_sdk_pi.types.dimension_key_detail.DimensionKeyDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDetailList) -> list:
    import aws_sdk_pi.types.dimension_key_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.dimension_key_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionKeyDetailList:
    import aws_sdk_pi.types.dimension_key_detail

    out: DimensionKeyDetailList = []
    for item in data:
        out.append(aws_sdk_pi.types.dimension_key_detail.deserialize_aws_json_1_1(item))
    return out

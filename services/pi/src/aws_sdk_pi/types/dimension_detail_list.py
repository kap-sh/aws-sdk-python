"""Generated from Smithy shape ``com.amazonaws.pi#DimensionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_detail

DimensionDetailList: TypeAlias = list[
    "aws_sdk_pi.types.dimension_detail.DimensionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionDetailList) -> list:
    import aws_sdk_pi.types.dimension_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.dimension_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionDetailList:
    import aws_sdk_pi.types.dimension_detail

    out: DimensionDetailList = []
    for item in data:
        out.append(aws_sdk_pi.types.dimension_detail.deserialize_aws_json_1_1(item))
    return out

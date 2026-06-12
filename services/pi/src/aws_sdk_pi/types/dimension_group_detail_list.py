"""Generated from Smithy shape ``com.amazonaws.pi#DimensionGroupDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_group_detail

DimensionGroupDetailList: TypeAlias = list[
    "aws_sdk_pi.types.dimension_group_detail.DimensionGroupDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionGroupDetailList) -> list:
    import aws_sdk_pi.types.dimension_group_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_pi.types.dimension_group_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionGroupDetailList:
    import aws_sdk_pi.types.dimension_group_detail

    out: DimensionGroupDetailList = []
    for item in data:
        out.append(
            aws_sdk_pi.types.dimension_group_detail.deserialize_aws_json_1_1(item)
        )
    return out

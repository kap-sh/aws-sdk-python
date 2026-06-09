"""Generated from Smithy shape ``com.amazonaws.kms#MultiRegionKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kms.types.multi_region_key

MultiRegionKeyList: TypeAlias = list[
    "aws_sdk_kms.types.multi_region_key.MultiRegionKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionKeyList) -> list:
    import aws_sdk_kms.types.multi_region_key

    out: list = []
    for item in value:
        out.append(aws_sdk_kms.types.multi_region_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MultiRegionKeyList:
    import aws_sdk_kms.types.multi_region_key

    out: MultiRegionKeyList = []
    for item in data:
        out.append(aws_sdk_kms.types.multi_region_key.deserialize_aws_json_1_1(item))
    return out

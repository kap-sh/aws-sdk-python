"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.pool_info

PoolInfos: TypeAlias = list["aws_sdk_storage_gateway.types.pool_info.PoolInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoolInfos) -> list:
    import aws_sdk_storage_gateway.types.pool_info

    out: list = []
    for item in value:
        out.append(aws_sdk_storage_gateway.types.pool_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PoolInfos:
    import aws_sdk_storage_gateway.types.pool_info

    out: PoolInfos = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.pool_info.deserialize_aws_json_1_1(item)
        )
    return out

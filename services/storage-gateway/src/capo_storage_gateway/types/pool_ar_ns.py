"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolARNs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.pool_arn

PoolARNs: TypeAlias = list["capo_storage_gateway.types.pool_arn.PoolARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoolARNs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PoolARNs:
    return list(data)

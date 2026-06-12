"""Generated from Smithy shape ``com.amazonaws.lakeformation#StorageOptimizerConfigMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.optimizer_type
    import aws_sdk_lakeformation.types.storage_optimizer_config

StorageOptimizerConfigMap: TypeAlias = dict[
    "aws_sdk_lakeformation.types.optimizer_type.OptimizerType",
    "aws_sdk_lakeformation.types.storage_optimizer_config.StorageOptimizerConfig",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StorageOptimizerConfigMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_lakeformation.types.optimizer_type
        import aws_sdk_lakeformation.types.storage_optimizer_config

        out[aws_sdk_lakeformation.types.optimizer_type.serialize_json(key)] = (
            aws_sdk_lakeformation.types.storage_optimizer_config.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> StorageOptimizerConfigMap:
    out: StorageOptimizerConfigMap = {}
    for key, value in data.items():
        import aws_sdk_lakeformation.types.optimizer_type
        import aws_sdk_lakeformation.types.storage_optimizer_config

        out[aws_sdk_lakeformation.types.optimizer_type.deserialize_json(key)] = (
            aws_sdk_lakeformation.types.storage_optimizer_config.deserialize_json(value)
        )
    return out

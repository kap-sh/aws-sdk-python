"""Generated from Smithy shape ``com.amazonaws.lakeformation#StorageOptimizerConfigMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.optimizer_type
    import capo_lakeformation.types.storage_optimizer_config

StorageOptimizerConfigMap: TypeAlias = dict[
    "capo_lakeformation.types.optimizer_type.OptimizerType",
    "capo_lakeformation.types.storage_optimizer_config.StorageOptimizerConfig",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StorageOptimizerConfigMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lakeformation.types.optimizer_type
        import capo_lakeformation.types.storage_optimizer_config

        out[capo_lakeformation.types.optimizer_type.serialize_json(key)] = (
            capo_lakeformation.types.storage_optimizer_config.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> StorageOptimizerConfigMap:
    out: StorageOptimizerConfigMap = {}
    for key, value in data.items():
        import capo_lakeformation.types.optimizer_type
        import capo_lakeformation.types.storage_optimizer_config

        out[capo_lakeformation.types.optimizer_type.deserialize_json(key)] = (
            capo_lakeformation.types.storage_optimizer_config.deserialize_json(value)
        )
    return out

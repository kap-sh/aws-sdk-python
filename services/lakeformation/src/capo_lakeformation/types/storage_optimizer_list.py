"""Generated from Smithy shape ``com.amazonaws.lakeformation#StorageOptimizerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.storage_optimizer

StorageOptimizerList: TypeAlias = list[
    "capo_lakeformation.types.storage_optimizer.StorageOptimizer"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageOptimizerList) -> list:
    import capo_lakeformation.types.storage_optimizer

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.storage_optimizer.serialize_json(item))
    return out


def deserialize_json(data: list) -> StorageOptimizerList:
    import capo_lakeformation.types.storage_optimizer

    out: StorageOptimizerList = []
    for item in data:
        out.append(capo_lakeformation.types.storage_optimizer.deserialize_json(item))
    return out

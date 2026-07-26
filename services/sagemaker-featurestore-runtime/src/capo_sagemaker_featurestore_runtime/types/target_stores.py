"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TargetStores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.target_store

TargetStores: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.target_store.TargetStore"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStores) -> list:
    import capo_sagemaker_featurestore_runtime.types.target_store

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.target_store.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetStores:
    import capo_sagemaker_featurestore_runtime.types.target_store

    out: TargetStores = []
    for item in data:
        out.append(
            capo_sagemaker_featurestore_runtime.types.target_store.deserialize_json(
                item
            )
        )
    return out

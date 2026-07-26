"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#Record``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_value

Record: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.feature_value.FeatureValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> list:
    import capo_sagemaker_featurestore_runtime.types.feature_value

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.feature_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Record:
    import capo_sagemaker_featurestore_runtime.types.feature_value

    out: Record = []
    for item in data:
        out.append(
            capo_sagemaker_featurestore_runtime.types.feature_value.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#FeatureNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_name

FeatureNames: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.feature_name.FeatureName"
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureNames) -> list:
    return list(value)


def deserialize_json(data: list) -> FeatureNames:
    return list(data)

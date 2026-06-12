"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ValueAsStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string

ValueAsStringList: TypeAlias = list[
    "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValueAsStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueAsStringList:
    return list(data)

"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#RecordIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string

RecordIdentifiers: TypeAlias = list[
    "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> RecordIdentifiers:
    return list(data)

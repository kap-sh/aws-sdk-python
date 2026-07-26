"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceDataImportStrategy``."""

from typing import Literal, TypeAlias, cast

InferenceDataImportStrategy: TypeAlias = Literal[
    "NO_IMPORT",
    "ADD_WHEN_EMPTY",
    "OVERWRITE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceDataImportStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferenceDataImportStrategy:
    return cast(InferenceDataImportStrategy, data)

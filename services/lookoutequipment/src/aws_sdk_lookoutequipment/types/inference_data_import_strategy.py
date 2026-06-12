"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceDataImportStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lookoutequipment.errors import DeserializationError

InferenceDataImportStrategy: TypeAlias = Literal[
    "NO_IMPORT",
    "ADD_WHEN_EMPTY",
    "OVERWRITE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_IMPORT",
        "ADD_WHEN_EMPTY",
        "OVERWRITE",
    )
)


def serialize_aws_json_1_0(value: InferenceDataImportStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferenceDataImportStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InferenceDataImportStrategy value: {data!r}"
        )
    return cast(InferenceDataImportStrategy, data)

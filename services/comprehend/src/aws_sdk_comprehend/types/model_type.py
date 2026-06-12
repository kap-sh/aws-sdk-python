"""Generated from Smithy shape ``com.amazonaws.comprehend#ModelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

ModelType: TypeAlias = Literal[
    "DOCUMENT_CLASSIFIER",
    "ENTITY_RECOGNIZER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT_CLASSIFIER",
        "ENTITY_RECOGNIZER",
    )
)


def serialize_aws_json_1_1(value: ModelType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelType value: {data!r}")
    return cast(ModelType, data)

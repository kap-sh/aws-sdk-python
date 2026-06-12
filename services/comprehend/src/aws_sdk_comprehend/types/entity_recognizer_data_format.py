"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

EntityRecognizerDataFormat: TypeAlias = Literal[
    "COMPREHEND_CSV",
    "AUGMENTED_MANIFEST",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPREHEND_CSV",
        "AUGMENTED_MANIFEST",
    )
)


def serialize_aws_json_1_1(value: EntityRecognizerDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityRecognizerDataFormat:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EntityRecognizerDataFormat value: {data!r}"
        )
    return cast(EntityRecognizerDataFormat, data)

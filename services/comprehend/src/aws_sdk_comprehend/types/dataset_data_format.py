"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetDataFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DatasetDataFormat: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: DatasetDataFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatasetDataFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetDataFormat value: {data!r}")
    return cast(DatasetDataFormat, data)

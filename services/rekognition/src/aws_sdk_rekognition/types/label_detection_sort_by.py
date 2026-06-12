"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

LabelDetectionSortBy: TypeAlias = Literal[
    "NAME",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: LabelDetectionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LabelDetectionSortBy value: {data!r}")
    return cast(LabelDetectionSortBy, data)

"""Generated from Smithy shape ``com.amazonaws.rekognition#CelebrityRecognitionSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

CelebrityRecognitionSortBy: TypeAlias = Literal[
    "ID",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ID",
        "TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: CelebrityRecognitionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CelebrityRecognitionSortBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CelebrityRecognitionSortBy value: {data!r}"
        )
    return cast(CelebrityRecognitionSortBy, data)

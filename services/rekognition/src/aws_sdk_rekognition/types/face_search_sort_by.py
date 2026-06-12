"""Generated from Smithy shape ``com.amazonaws.rekognition#FaceSearchSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

FaceSearchSortBy: TypeAlias = Literal[
    "INDEX",
    "TIMESTAMP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDEX",
        "TIMESTAMP",
    )
)


def serialize_aws_json_1_1(value: FaceSearchSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FaceSearchSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FaceSearchSortBy value: {data!r}")
    return cast(FaceSearchSortBy, data)

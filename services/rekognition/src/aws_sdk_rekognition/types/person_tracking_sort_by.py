"""Generated from Smithy shape ``com.amazonaws.rekognition#PersonTrackingSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rekognition.errors import DeserializationError

PersonTrackingSortBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: PersonTrackingSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PersonTrackingSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PersonTrackingSortBy value: {data!r}")
    return cast(PersonTrackingSortBy, data)

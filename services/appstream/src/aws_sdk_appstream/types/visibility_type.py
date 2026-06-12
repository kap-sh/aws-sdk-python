"""Generated from Smithy shape ``com.amazonaws.appstream#VisibilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

VisibilityType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
    "SHARED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE",
        "SHARED",
    )
)


def serialize_aws_json_1_1(value: VisibilityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VisibilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VisibilityType value: {data!r}")
    return cast(VisibilityType, data)

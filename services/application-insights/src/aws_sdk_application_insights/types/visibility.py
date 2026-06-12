"""Generated from Smithy shape ``com.amazonaws.applicationinsights#Visibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

Visibility: TypeAlias = Literal[
    "IGNORED",
    "VISIBLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORED",
        "VISIBLE",
    )
)


def serialize_aws_json_1_1(value: Visibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Visibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Visibility value: {data!r}")
    return cast(Visibility, data)

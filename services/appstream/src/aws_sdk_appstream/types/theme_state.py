"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ThemeState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: ThemeState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThemeState value: {data!r}")
    return cast(ThemeState, data)

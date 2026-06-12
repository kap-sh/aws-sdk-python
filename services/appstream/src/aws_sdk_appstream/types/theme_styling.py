"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeStyling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ThemeStyling: TypeAlias = Literal[
    "LIGHT_BLUE",
    "BLUE",
    "PINK",
    "RED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LIGHT_BLUE",
        "BLUE",
        "PINK",
        "RED",
    )
)


def serialize_aws_json_1_1(value: ThemeStyling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeStyling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThemeStyling value: {data!r}")
    return cast(ThemeStyling, data)

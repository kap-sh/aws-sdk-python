"""Generated from Smithy shape ``com.amazonaws.appstream#AppVisibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AppVisibility: TypeAlias = Literal[
    "ALL",
    "ASSOCIATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "ASSOCIATED",
    )
)


def serialize_aws_json_1_1(value: AppVisibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppVisibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppVisibility value: {data!r}")
    return cast(AppVisibility, data)

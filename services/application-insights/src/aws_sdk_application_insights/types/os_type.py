"""Generated from Smithy shape ``com.amazonaws.applicationinsights#OsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

OsType: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LINUX",
    )
)


def serialize_aws_json_1_1(value: OsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OsType value: {data!r}")
    return cast(OsType, data)

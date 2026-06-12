"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluenceVersion: TypeAlias = Literal[
    "CLOUD",
    "SERVER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUD",
        "SERVER",
    )
)


def serialize_aws_json_1_1(value: ConfluenceVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluenceVersion value: {data!r}")
    return cast(ConfluenceVersion, data)

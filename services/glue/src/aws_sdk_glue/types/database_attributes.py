"""Generated from Smithy shape ``com.amazonaws.glue#DatabaseAttributes``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DatabaseAttributes: TypeAlias = Literal[
    "NAME",
    "TARGET_DATABASE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAME",
        "TARGET_DATABASE",
    )
)


def serialize_aws_json_1_1(value: DatabaseAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseAttributes:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseAttributes value: {data!r}")
    return cast(DatabaseAttributes, data)

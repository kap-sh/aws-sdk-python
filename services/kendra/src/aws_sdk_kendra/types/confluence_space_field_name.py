"""Generated from Smithy shape ``com.amazonaws.kendra#ConfluenceSpaceFieldName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

ConfluenceSpaceFieldName: TypeAlias = Literal[
    "DISPLAY_URL",
    "ITEM_TYPE",
    "SPACE_KEY",
    "URL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISPLAY_URL",
        "ITEM_TYPE",
        "SPACE_KEY",
        "URL",
    )
)


def serialize_aws_json_1_1(value: ConfluenceSpaceFieldName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfluenceSpaceFieldName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfluenceSpaceFieldName value: {data!r}")
    return cast(ConfluenceSpaceFieldName, data)

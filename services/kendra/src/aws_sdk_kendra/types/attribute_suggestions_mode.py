"""Generated from Smithy shape ``com.amazonaws.kendra#AttributeSuggestionsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

AttributeSuggestionsMode: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: AttributeSuggestionsMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeSuggestionsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeSuggestionsMode value: {data!r}")
    return cast(AttributeSuggestionsMode, data)

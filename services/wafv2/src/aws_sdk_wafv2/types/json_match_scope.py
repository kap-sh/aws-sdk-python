"""Generated from Smithy shape ``com.amazonaws.wafv2#JsonMatchScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

JsonMatchScope: TypeAlias = Literal[
    "ALL",
    "KEY",
    "VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "KEY",
        "VALUE",
    )
)


def serialize_aws_json_1_1(value: JsonMatchScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JsonMatchScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JsonMatchScope value: {data!r}")
    return cast(JsonMatchScope, data)

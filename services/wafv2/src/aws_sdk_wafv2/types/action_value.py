"""Generated from Smithy shape ``com.amazonaws.wafv2#ActionValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

ActionValue: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
    "COUNT",
    "CAPTCHA",
    "CHALLENGE",
    "EXCLUDED_AS_COUNT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "BLOCK",
        "COUNT",
        "CAPTCHA",
        "CHALLENGE",
        "EXCLUDED_AS_COUNT",
    )
)


def serialize_aws_json_1_1(value: ActionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionValue value: {data!r}")
    return cast(ActionValue, data)

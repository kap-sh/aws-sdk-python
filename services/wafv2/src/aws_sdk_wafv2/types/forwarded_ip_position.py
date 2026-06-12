"""Generated from Smithy shape ``com.amazonaws.wafv2#ForwardedIPPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

ForwardedIPPosition: TypeAlias = Literal[
    "FIRST",
    "LAST",
    "ANY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIRST",
        "LAST",
        "ANY",
    )
)


def serialize_aws_json_1_1(value: ForwardedIPPosition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ForwardedIPPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ForwardedIPPosition value: {data!r}")
    return cast(ForwardedIPPosition, data)

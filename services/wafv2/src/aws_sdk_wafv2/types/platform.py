"""Generated from Smithy shape ``com.amazonaws.wafv2#Platform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

Platform: TypeAlias = Literal[
    "IOS",
    "ANDROID",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IOS",
        "ANDROID",
    )
)


def serialize_aws_json_1_1(value: Platform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Platform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Platform value: {data!r}")
    return cast(Platform, data)

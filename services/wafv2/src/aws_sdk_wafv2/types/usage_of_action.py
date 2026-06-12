"""Generated from Smithy shape ``com.amazonaws.wafv2#UsageOfAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

UsageOfAction: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: UsageOfAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UsageOfAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsageOfAction value: {data!r}")
    return cast(UsageOfAction, data)

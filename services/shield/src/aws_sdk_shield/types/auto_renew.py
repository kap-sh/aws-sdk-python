"""Generated from Smithy shape ``com.amazonaws.shield#AutoRenew``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

AutoRenew: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AutoRenew) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoRenew:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRenew value: {data!r}")
    return cast(AutoRenew, data)

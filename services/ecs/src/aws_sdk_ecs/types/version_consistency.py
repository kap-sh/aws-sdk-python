"""Generated from Smithy shape ``com.amazonaws.ecs#VersionConsistency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ecs.errors import DeserializationError

VersionConsistency: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def serialize_aws_json_1_1(value: VersionConsistency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VersionConsistency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VersionConsistency value: {data!r}")
    return cast(VersionConsistency, data)

"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ScopeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

ScopeName: TypeAlias = Literal[
    "Organization",
    "AccountId",
    "ResourceArn",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Organization",
        "AccountId",
        "ResourceArn",
    )
)


def serialize_aws_json_1_0(value: ScopeName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScopeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScopeName value: {data!r}")
    return cast(ScopeName, data)

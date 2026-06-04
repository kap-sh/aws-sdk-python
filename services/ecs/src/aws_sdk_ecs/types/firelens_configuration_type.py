"""Generated from Smithy shape ``com.amazonaws.ecs#FirelensConfigurationType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

FirelensConfigurationType: TypeAlias = Literal[
    "fluentd",
    "fluentbit",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "fluentd",
        "fluentbit",
    )
)


def serialize_aws_json_1_1(value: FirelensConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirelensConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirelensConfigurationType value: {data!r}")
    return cast(FirelensConfigurationType, data)

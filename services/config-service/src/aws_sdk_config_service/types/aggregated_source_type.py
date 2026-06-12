"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

AggregatedSourceType: TypeAlias = Literal[
    "ACCOUNT",
    "ORGANIZATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORGANIZATION",
    )
)


def serialize_aws_json_1_1(value: AggregatedSourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatedSourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregatedSourceType value: {data!r}")
    return cast(AggregatedSourceType, data)

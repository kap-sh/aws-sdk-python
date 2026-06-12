"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatedSourceStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

AggregatedSourceStatusType: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "OUTDATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "SUCCEEDED",
        "OUTDATED",
    )
)


def serialize_aws_json_1_1(value: AggregatedSourceStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatedSourceStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AggregatedSourceStatusType value: {data!r}"
        )
    return cast(AggregatedSourceStatusType, data)

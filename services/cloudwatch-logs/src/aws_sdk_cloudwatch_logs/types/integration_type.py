"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

IntegrationType: TypeAlias = Literal["OPENSEARCH",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPENSEARCH",))


def serialize_aws_json_1_1(value: IntegrationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IntegrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IntegrationType value: {data!r}")
    return cast(IntegrationType, data)

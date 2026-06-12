"""Generated from Smithy shape ``com.amazonaws.configservice#AggregatorFilterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

AggregatorFilterType: TypeAlias = Literal["INCLUDE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("INCLUDE",))


def serialize_aws_json_1_1(value: AggregatorFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AggregatorFilterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AggregatorFilterType value: {data!r}")
    return cast(AggregatorFilterType, data)

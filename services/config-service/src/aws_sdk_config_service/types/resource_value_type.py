"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ResourceValueType: TypeAlias = Literal["RESOURCE_ID",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOURCE_ID",))


def serialize_aws_json_1_1(value: ResourceValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceValueType value: {data!r}")
    return cast(ResourceValueType, data)

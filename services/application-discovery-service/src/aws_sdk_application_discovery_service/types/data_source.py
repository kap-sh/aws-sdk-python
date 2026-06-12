"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DataSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

DataSource: TypeAlias = Literal["AGENT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AGENT",))


def serialize_aws_json_1_1(value: DataSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataSource value: {data!r}")
    return cast(DataSource, data)

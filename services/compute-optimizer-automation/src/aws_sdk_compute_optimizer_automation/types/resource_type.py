"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer_automation.errors import DeserializationError

ResourceType: TypeAlias = Literal["EbsVolume",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("EbsVolume",))


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)

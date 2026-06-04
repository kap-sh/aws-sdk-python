"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterSettingName``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

ClusterSettingName: TypeAlias = Literal["containerInsights",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("containerInsights",))


def serialize_aws_json_1_1(value: ClusterSettingName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterSettingName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterSettingName value: {data!r}")
    return cast(ClusterSettingName, data)

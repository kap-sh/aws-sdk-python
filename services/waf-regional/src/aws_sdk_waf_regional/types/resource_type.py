"""Generated from Smithy shape ``com.amazonaws.wafregional#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_waf_regional.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "APPLICATION_LOAD_BALANCER",
    "API_GATEWAY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLICATION_LOAD_BALANCER",
        "API_GATEWAY",
    )
)


def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)

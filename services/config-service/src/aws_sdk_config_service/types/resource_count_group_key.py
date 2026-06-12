"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceCountGroupKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ResourceCountGroupKey: TypeAlias = Literal[
    "RESOURCE_TYPE",
    "ACCOUNT_ID",
    "AWS_REGION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE_TYPE",
        "ACCOUNT_ID",
        "AWS_REGION",
    )
)


def serialize_aws_json_1_1(value: ResourceCountGroupKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceCountGroupKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceCountGroupKey value: {data!r}")
    return cast(ResourceCountGroupKey, data)

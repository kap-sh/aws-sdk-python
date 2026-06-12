"""Generated from Smithy shape ``com.amazonaws.identitystore#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "GROUP",
    "USER",
    "IDENTITY_STORE",
    "GROUP_MEMBERSHIP",
    "RESOURCE_POLICY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GROUP",
        "USER",
        "IDENTITY_STORE",
        "GROUP_MEMBERSHIP",
        "RESOURCE_POLICY",
    )
)


def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)

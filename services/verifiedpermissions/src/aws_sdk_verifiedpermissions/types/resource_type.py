"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "IDENTITY_SOURCE",
    "POLICY_STORE",
    "POLICY",
    "POLICY_TEMPLATE",
    "SCHEMA",
    "POLICY_STORE_ALIAS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDENTITY_SOURCE",
        "POLICY_STORE",
        "POLICY",
        "POLICY_TEMPLATE",
        "SCHEMA",
        "POLICY_STORE_ALIAS",
    )
)


def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)

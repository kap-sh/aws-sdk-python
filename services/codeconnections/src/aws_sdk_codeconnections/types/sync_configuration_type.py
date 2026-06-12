"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncConfigurationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeconnections.errors import DeserializationError

SyncConfigurationType: TypeAlias = Literal["CFN_STACK_SYNC",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CFN_STACK_SYNC",))


def serialize_aws_json_1_0(value: SyncConfigurationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SyncConfigurationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SyncConfigurationType value: {data!r}")
    return cast(SyncConfigurationType, data)

"""Generated from Smithy shape ``com.amazonaws.directoryservice#ReplicationScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

ReplicationScope: TypeAlias = Literal["Domain",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Domain",))


def serialize_aws_json_1_1(value: ReplicationScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReplicationScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReplicationScope value: {data!r}")
    return cast(ReplicationScope, data)

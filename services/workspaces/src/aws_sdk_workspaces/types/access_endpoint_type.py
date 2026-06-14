"""Generated from Smithy shape ``com.amazonaws.workspaces#AccessEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

AccessEndpointType: TypeAlias = Literal["STREAMING_WSP",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STREAMING_WSP",))


def serialize_aws_json_1_1(value: AccessEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessEndpointType value: {data!r}")
    return cast(AccessEndpointType, data)

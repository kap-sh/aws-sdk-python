"""Generated from Smithy shape ``com.amazonaws.appstream#AccessEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

AccessEndpointType: TypeAlias = Literal["STREAMING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("STREAMING",))


def serialize_aws_json_1_1(value: AccessEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessEndpointType value: {data!r}")
    return cast(AccessEndpointType, data)

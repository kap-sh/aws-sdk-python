"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_interconnect.errors import DeserializationError

AttachPointType: TypeAlias = Literal["DirectConnectGateway",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("DirectConnectGateway",))


def serialize_aws_json_1_0(value: AttachPointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttachPointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttachPointType value: {data!r}")
    return cast(AttachPointType, data)

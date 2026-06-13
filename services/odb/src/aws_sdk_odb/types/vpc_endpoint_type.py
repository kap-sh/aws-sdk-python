"""Generated from Smithy shape ``com.amazonaws.odb#VpcEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

VpcEndpointType: TypeAlias = Literal["SERVICENETWORK",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SERVICENETWORK",))


def serialize_aws_json_1_0(value: VpcEndpointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VpcEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcEndpointType value: {data!r}")
    return cast(VpcEndpointType, data)

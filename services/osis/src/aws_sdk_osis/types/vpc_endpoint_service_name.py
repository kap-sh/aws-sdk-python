"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpointServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_osis.errors import DeserializationError

VpcEndpointServiceName: TypeAlias = Literal["OPENSEARCH_SERVERLESS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPENSEARCH_SERVERLESS",))


def serialize_json(value: VpcEndpointServiceName) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcEndpointServiceName value: {data!r}")
    return cast(VpcEndpointServiceName, data)

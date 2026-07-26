"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpointServiceName``."""

from typing import Literal, TypeAlias, cast

VpcEndpointServiceName: TypeAlias = Literal["OPENSEARCH_SERVERLESS",]


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpointServiceName) -> str:
    return value


def deserialize_json(data: str) -> VpcEndpointServiceName:
    return cast(VpcEndpointServiceName, data)

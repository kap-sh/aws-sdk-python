"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#RevokeVpcEndpointAccessResponse``."""

from typing import TypedDict


class RevokeVpcEndpointAccessResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RevokeVpcEndpointAccessResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokeVpcEndpointAccessResponse:
    out: RevokeVpcEndpointAccessResponse = {}  # type: ignore[typeddict-item]
    return out

"""Generated from Smithy shape ``com.amazonaws.securityagent#EndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.endpoint

EndpointList: TypeAlias = list["capo_securityagent.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointList) -> list:
    import capo_securityagent.types.endpoint

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> EndpointList:
    import capo_securityagent.types.endpoint

    out: EndpointList = []
    for item in data:
        out.append(capo_securityagent.types.endpoint.deserialize_json(item))
    return out

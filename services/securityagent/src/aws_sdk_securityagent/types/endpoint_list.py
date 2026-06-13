"""Generated from Smithy shape ``com.amazonaws.securityagent#EndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.endpoint

EndpointList: TypeAlias = list["aws_sdk_securityagent.types.endpoint.Endpoint"]


# --- restJson1 ser/de ---
def serialize_json(value: EndpointList) -> list:
    import aws_sdk_securityagent.types.endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_securityagent.types.endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> EndpointList:
    import aws_sdk_securityagent.types.endpoint

    out: EndpointList = []
    for item in data:
        out.append(aws_sdk_securityagent.types.endpoint.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.osis#ServiceVpcEndpointsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_osis.types.service_vpc_endpoint

ServiceVpcEndpointsList: TypeAlias = list[
    "aws_sdk_osis.types.service_vpc_endpoint.ServiceVpcEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceVpcEndpointsList) -> list:
    import aws_sdk_osis.types.service_vpc_endpoint

    out: list = []
    for item in value:
        out.append(aws_sdk_osis.types.service_vpc_endpoint.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceVpcEndpointsList:
    import aws_sdk_osis.types.service_vpc_endpoint

    out: ServiceVpcEndpointsList = []
    for item in data:
        out.append(aws_sdk_osis.types.service_vpc_endpoint.deserialize_json(item))
    return out

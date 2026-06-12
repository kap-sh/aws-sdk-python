"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfVpcLink``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.vpc_link

ListOfVpcLink: TypeAlias = list["aws_sdk_api_gateway.types.vpc_link.VpcLink"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfVpcLink) -> list:
    import aws_sdk_api_gateway.types.vpc_link

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.vpc_link.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfVpcLink:
    import aws_sdk_api_gateway.types.vpc_link

    out: ListOfVpcLink = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.vpc_link.deserialize_json(item))
    return out

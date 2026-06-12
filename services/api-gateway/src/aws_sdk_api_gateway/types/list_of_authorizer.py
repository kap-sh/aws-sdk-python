"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfAuthorizer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.authorizer

ListOfAuthorizer: TypeAlias = list["aws_sdk_api_gateway.types.authorizer.Authorizer"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfAuthorizer) -> list:
    import aws_sdk_api_gateway.types.authorizer

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.authorizer.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfAuthorizer:
    import aws_sdk_api_gateway.types.authorizer

    out: ListOfAuthorizer = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.authorizer.deserialize_json(item))
    return out

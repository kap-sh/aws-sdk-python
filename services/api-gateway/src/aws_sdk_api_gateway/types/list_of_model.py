"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfModel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.model

ListOfModel: TypeAlias = list["aws_sdk_api_gateway.types.model.Model"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfModel) -> list:
    import aws_sdk_api_gateway.types.model

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.model.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfModel:
    import aws_sdk_api_gateway.types.model

    out: ListOfModel = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.model.deserialize_json(item))
    return out

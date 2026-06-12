"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfModel``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.model

__listOfModel: TypeAlias = list["aws_sdk_apigatewayv2.types.model.Model"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfModel) -> list:
    import aws_sdk_apigatewayv2.types.model

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.model.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfModel:
    import aws_sdk_apigatewayv2.types.model

    out: __listOfModel = []
    for item in data:
        out.append(aws_sdk_apigatewayv2.types.model.deserialize_json(item))
    return out

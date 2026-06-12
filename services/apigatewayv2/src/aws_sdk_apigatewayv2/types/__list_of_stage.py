"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.stage

__listOfStage: TypeAlias = list["aws_sdk_apigatewayv2.types.stage.Stage"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfStage) -> list:
    import aws_sdk_apigatewayv2.types.stage

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfStage:
    import aws_sdk_apigatewayv2.types.stage

    out: __listOfStage = []
    for item in data:
        out.append(aws_sdk_apigatewayv2.types.stage.deserialize_json(item))
    return out

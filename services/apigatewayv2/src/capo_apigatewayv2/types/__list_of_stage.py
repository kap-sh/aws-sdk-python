"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfStage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.stage

__listOfStage: TypeAlias = list["capo_apigatewayv2.types.stage.Stage"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfStage) -> list:
    import capo_apigatewayv2.types.stage

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.stage.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfStage:
    import capo_apigatewayv2.types.stage

    out: __listOfStage = []
    for item in data:
        out.append(capo_apigatewayv2.types.stage.deserialize_json(item))
    return out

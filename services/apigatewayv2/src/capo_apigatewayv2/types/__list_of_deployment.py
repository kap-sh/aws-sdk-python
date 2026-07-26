"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfDeployment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.deployment

__listOfDeployment: TypeAlias = list["capo_apigatewayv2.types.deployment.Deployment"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDeployment) -> list:
    import capo_apigatewayv2.types.deployment

    out: list = []
    for item in value:
        out.append(capo_apigatewayv2.types.deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDeployment:
    import capo_apigatewayv2.types.deployment

    out: __listOfDeployment = []
    for item in data:
        out.append(capo_apigatewayv2.types.deployment.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfDeployment``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.deployment

__listOfDeployment: TypeAlias = list["aws_sdk_apigatewayv2.types.deployment.Deployment"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfDeployment) -> list:
    import aws_sdk_apigatewayv2.types.deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_apigatewayv2.types.deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfDeployment:
    import aws_sdk_apigatewayv2.types.deployment

    out: __listOfDeployment = []
    for item in data:
        out.append(aws_sdk_apigatewayv2.types.deployment.deserialize_json(item))
    return out

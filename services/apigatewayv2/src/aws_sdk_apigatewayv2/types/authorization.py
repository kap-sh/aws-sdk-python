"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Authorization``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.cognito_config
    import aws_sdk_apigatewayv2.types.none


class Authorization(TypedDict):
    cognito_config: NotRequired[
        "aws_sdk_apigatewayv2.types.cognito_config.CognitoConfig"
    ]
    """<p>The Amazon Cognito configuration.</p>"""
    none: NotRequired["aws_sdk_apigatewayv2.types.none.None_"]
    """<p>Provide no authorization for your portal. This makes your portal publicly accesible on the web.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Authorization) -> dict:
    out: dict = {}
    if "cognito_config" in value:
        import aws_sdk_apigatewayv2.types.cognito_config

        out["cognitoConfig"] = aws_sdk_apigatewayv2.types.cognito_config.serialize_json(
            value["cognito_config"]
        )
    if "none" in value:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.serialize_json(value["none"])
    return out


def deserialize_json(data: dict) -> Authorization:
    out: Authorization = {}  # type: ignore[typeddict-item]
    if "cognitoConfig" in data:
        import aws_sdk_apigatewayv2.types.cognito_config

        out["cognito_config"] = (
            aws_sdk_apigatewayv2.types.cognito_config.deserialize_json(
                data["cognitoConfig"]
            )
        )
    if "none" in data:
        import aws_sdk_apigatewayv2.types.none

        out["none"] = aws_sdk_apigatewayv2.types.none.deserialize_json(data["none"])
    return out

"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#Authorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.cognito_config
    import capo_apigatewayv2.types.none


class Authorization(TypedDict, closed=True):
    cognito_config: NotRequired["capo_apigatewayv2.types.cognito_config.CognitoConfig"]
    """<p>The Amazon Cognito configuration.</p>"""
    none: NotRequired["capo_apigatewayv2.types.none.None_"]
    """<p>Provide no authorization for your portal. This makes your portal publicly accesible on the web.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Authorization) -> dict:
    out: dict = {}
    if "cognito_config" in value:
        import capo_apigatewayv2.types.cognito_config

        out["cognitoConfig"] = capo_apigatewayv2.types.cognito_config.serialize_json(
            value["cognito_config"]
        )
    if "none" in value:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.serialize_json(value["none"])
    return out


def deserialize_json(data: dict) -> Authorization:
    out: Authorization = {}  # type: ignore[typeddict-item]
    if "cognitoConfig" in data:
        import capo_apigatewayv2.types.cognito_config

        out["cognito_config"] = capo_apigatewayv2.types.cognito_config.deserialize_json(
            data["cognitoConfig"]
        )
    if "none" in data:
        import capo_apigatewayv2.types.none

        out["none"] = capo_apigatewayv2.types.none.deserialize_json(data["none"])
    return out

"""Generated from Smithy shape ``com.amazonaws.appflow#OAuthProperties``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.auth_code_url
    import aws_sdk_appflow.types.o_auth_scope_list
    import aws_sdk_appflow.types.token_url


class OAuthProperties(TypedDict):
    token_url: "aws_sdk_appflow.types.token_url.TokenUrl"
    """<p> The token url required to fetch access/refresh tokens using authorization code and also to refresh expired access token using refresh token.</p>"""
    auth_code_url: "aws_sdk_appflow.types.auth_code_url.AuthCodeUrl"
    """<p> The authorization code url required to redirect to SAP Login Page to fetch authorization code for OAuth type authentication. </p>"""
    o_auth_scopes: "aws_sdk_appflow.types.o_auth_scope_list.OAuthScopeList"
    """<p> The OAuth scopes required for OAuth type authentication. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthProperties) -> dict:
    out: dict = {}
    out["tokenUrl"] = value["token_url"]
    out["authCodeUrl"] = value["auth_code_url"]
    import aws_sdk_appflow.types.o_auth_scope_list

    out["oAuthScopes"] = aws_sdk_appflow.types.o_auth_scope_list.serialize_json(
        value["o_auth_scopes"]
    )
    return out


def deserialize_json(data: dict) -> OAuthProperties:
    out: OAuthProperties = {}  # type: ignore[typeddict-item]
    if "tokenUrl" in data:
        out["token_url"] = data["tokenUrl"]
    else:
        raise DeserializationError("OAuthProperties.token_url required")
    if "authCodeUrl" in data:
        out["auth_code_url"] = data["authCodeUrl"]
    else:
        raise DeserializationError("OAuthProperties.auth_code_url required")
    if "oAuthScopes" in data:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["o_auth_scopes"] = aws_sdk_appflow.types.o_auth_scope_list.deserialize_json(
            data["oAuthScopes"]
        )
    else:
        raise DeserializationError("OAuthProperties.o_auth_scopes required")
    return out

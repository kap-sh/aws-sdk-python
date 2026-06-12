"""Generated from Smithy shape ``com.amazonaws.appfabric#ConnectAppAuthorizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.auth_request
    import aws_sdk_appfabric.types.identifier


class ConnectAppAuthorizationRequest(TypedDict):
    app_bundle_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle that contains the app authorization to use for the request.</p>"""
    app_authorization_identifier: "aws_sdk_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app authorization to use for the request.</p>"""
    auth_request: NotRequired["aws_sdk_appfabric.types.auth_request.AuthRequest"]
    """<p>Contains OAuth2 authorization information.</p> <p>This is required if the app authorization for the request is configured with an OAuth2 (<code>oauth2</code>) authorization type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectAppAuthorizationRequest) -> dict:
    out: dict = {}
    if "auth_request" in value:
        import aws_sdk_appfabric.types.auth_request

        out["authRequest"] = aws_sdk_appfabric.types.auth_request.serialize_json(
            value["auth_request"]
        )
    return out


def deserialize_json(data: dict) -> ConnectAppAuthorizationRequest:
    out: ConnectAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if "authRequest" in data:
        import aws_sdk_appfabric.types.auth_request

        out["auth_request"] = aws_sdk_appfabric.types.auth_request.deserialize_json(
            data["authRequest"]
        )
    return out

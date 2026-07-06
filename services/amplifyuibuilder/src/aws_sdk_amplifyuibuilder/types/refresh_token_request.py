"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#RefreshTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.refresh_token_request_body
    import aws_sdk_amplifyuibuilder.types.token_providers


class RefreshTokenRequest(TypedDict, closed=True):
    provider: "aws_sdk_amplifyuibuilder.types.token_providers.TokenProviders"
    """<p>The third-party provider for the token. The only valid value is <code>figma</code>.</p>"""
    refresh_token_body: "aws_sdk_amplifyuibuilder.types.refresh_token_request_body.RefreshTokenRequestBody"
    """<p>Information about the refresh token request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RefreshTokenRequest) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.refresh_token_request_body

    out["refreshTokenBody"] = (
        aws_sdk_amplifyuibuilder.types.refresh_token_request_body.serialize_json(
            value["refresh_token_body"]
        )
    )
    return out


def deserialize_json(data: dict) -> RefreshTokenRequest:
    out: RefreshTokenRequest = {}  # type: ignore[typeddict-item]
    if "refreshTokenBody" in data:
        import aws_sdk_amplifyuibuilder.types.refresh_token_request_body

        out["refresh_token_body"] = (
            aws_sdk_amplifyuibuilder.types.refresh_token_request_body.deserialize_json(
                data["refreshTokenBody"]
            )
        )
    else:
        raise DeserializationError("RefreshTokenRequest.refresh_token_body required")
    return out

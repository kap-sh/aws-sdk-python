"""Generated from Smithy shape ``com.amazonaws.connect#Credentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_token
    import aws_sdk_connect.types.timestamp


class Credentials(TypedDict, closed=True):
    access_token: NotRequired["aws_sdk_connect.types.security_token.SecurityToken"]
    """<p>An access token generated for a federated user to access Connect Customer.</p>"""
    access_token_expiration: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>A token generated with an expiration time for the session a user is logged in to Connect Customer.</p>"""
    refresh_token: NotRequired["aws_sdk_connect.types.security_token.SecurityToken"]
    """<p>Renews a token generated for a user to access the Connect Customer instance.</p>"""
    refresh_token_expiration: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>Renews the expiration timer for a generated token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    if "access_token_expiration" in value:
        import aws_sdk_connect.types.timestamp

        out["AccessTokenExpiration"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["access_token_expiration"]
        )
    if "refresh_token" in value:
        out["RefreshToken"] = value["refresh_token"]
    if "refresh_token_expiration" in value:
        import aws_sdk_connect.types.timestamp

        out["RefreshTokenExpiration"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["refresh_token_expiration"]
        )
    return out


def deserialize_json(data: dict) -> Credentials:
    out: Credentials = {}  # type: ignore[typeddict-item]
    if "AccessToken" in data:
        out["access_token"] = data["AccessToken"]
    if "AccessTokenExpiration" in data:
        import aws_sdk_connect.types.timestamp

        out["access_token_expiration"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["AccessTokenExpiration"]
            )
        )
    if "RefreshToken" in data:
        out["refresh_token"] = data["RefreshToken"]
    if "RefreshTokenExpiration" in data:
        import aws_sdk_connect.types.timestamp

        out["refresh_token_expiration"] = (
            aws_sdk_connect.types.timestamp.deserialize_json(
                data["RefreshTokenExpiration"]
            )
        )
    return out

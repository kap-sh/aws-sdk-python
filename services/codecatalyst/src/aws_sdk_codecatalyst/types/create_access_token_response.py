"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateAccessTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.access_token_id
    import aws_sdk_codecatalyst.types.access_token_name
    import aws_sdk_codecatalyst.types.access_token_secret
    import aws_sdk_codecatalyst.types.timestamp


class CreateAccessTokenResponse(TypedDict, closed=True):
    secret: "aws_sdk_codecatalyst.types.access_token_secret.AccessTokenSecret"
    """<p>The secret value of the personal access token.</p>"""
    name: "aws_sdk_codecatalyst.types.access_token_name.AccessTokenName"
    """<p>The friendly name of the personal access token.</p>"""
    expires_time: "aws_sdk_codecatalyst.types.timestamp.Timestamp"
    r"""<p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>. If not specified, the default is one year from creation.</p>"""
    access_token_id: "aws_sdk_codecatalyst.types.access_token_id.AccessTokenId"
    """<p>The system-generated unique ID of the access token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenResponse) -> dict:
    out: dict = {}
    out["secret"] = value["secret"]
    out["name"] = value["name"]
    import aws_sdk_codecatalyst.types.timestamp

    out["expiresTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
        value["expires_time"]
    )
    out["accessTokenId"] = value["access_token_id"]
    return out


def deserialize_json(data: dict) -> CreateAccessTokenResponse:
    out: CreateAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if "secret" in data:
        out["secret"] = data["secret"]
    else:
        raise DeserializationError("CreateAccessTokenResponse.secret required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAccessTokenResponse.name required")
    if "expiresTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["expires_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["expiresTime"]
        )
    else:
        raise DeserializationError("CreateAccessTokenResponse.expires_time required")
    if "accessTokenId" in data:
        out["access_token_id"] = data["accessTokenId"]
    else:
        raise DeserializationError("CreateAccessTokenResponse.access_token_id required")
    return out

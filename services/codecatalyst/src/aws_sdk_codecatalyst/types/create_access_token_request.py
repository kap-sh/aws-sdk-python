"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateAccessTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.access_token_name
    import aws_sdk_codecatalyst.types.timestamp


class CreateAccessTokenRequest(TypedDict):
    name: "aws_sdk_codecatalyst.types.access_token_name.AccessTokenName"
    """<p>The friendly name of the personal access token.</p>"""
    expires_time: NotRequired["aws_sdk_codecatalyst.types.timestamp.Timestamp"]
    r"""<p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "expires_time" in value:
        import aws_sdk_codecatalyst.types.timestamp

        out["expiresTime"] = aws_sdk_codecatalyst.types.timestamp.serialize_json(
            value["expires_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessTokenRequest:
    out: CreateAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAccessTokenRequest.name required")
    if "expiresTime" in data:
        import aws_sdk_codecatalyst.types.timestamp

        out["expires_time"] = aws_sdk_codecatalyst.types.timestamp.deserialize_json(
            data["expiresTime"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.codecatalyst#AccessTokenSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_id
    import capo_codecatalyst.types.access_token_name
    import capo_codecatalyst.types.timestamp


class AccessTokenSummary(TypedDict, closed=True):
    id: "capo_codecatalyst.types.access_token_id.AccessTokenId"
    """<p>The system-generated ID of the personal access token.</p>"""
    name: "capo_codecatalyst.types.access_token_name.AccessTokenName"
    """<p>The friendly name of the personal access token.</p>"""
    expires_time: NotRequired["capo_codecatalyst.types.timestamp.Timestamp"]
    r"""<p>The date and time when the personal access token will expire, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessTokenSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "expires_time" in value:
        import capo_codecatalyst.types.timestamp

        out["expiresTime"] = capo_codecatalyst.types.timestamp.serialize_json(
            value["expires_time"]
        )
    return out


def deserialize_json(data: dict) -> AccessTokenSummary:
    out: AccessTokenSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessTokenSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AccessTokenSummary.name required")
    if "expiresTime" in data:
        import capo_codecatalyst.types.timestamp

        out["expires_time"] = capo_codecatalyst.types.timestamp.deserialize_json(
            data["expiresTime"]
        )
    return out

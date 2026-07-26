"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetAuthorizationTokenResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.string
    import capo_codeartifact.types.timestamp


class GetAuthorizationTokenResult(TypedDict, closed=True):
    authorization_token: NotRequired["capo_codeartifact.types.string.String"]
    """<p> The returned authentication token. </p>"""
    expiration: NotRequired["capo_codeartifact.types.timestamp.Timestamp"]
    """<p> A timestamp that specifies the date and time the authorization token expires. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthorizationTokenResult) -> dict:
    out: dict = {}
    if "authorization_token" in value:
        out["authorizationToken"] = value["authorization_token"]
    if "expiration" in value:
        import capo_codeartifact.types.timestamp

        out["expiration"] = capo_codeartifact.types.timestamp.serialize_json(
            value["expiration"]
        )
    return out


def deserialize_json(data: dict) -> GetAuthorizationTokenResult:
    out: GetAuthorizationTokenResult = {}  # type: ignore[typeddict-item]
    if "authorizationToken" in data:
        out["authorization_token"] = data["authorizationToken"]
    if "expiration" in data:
        import capo_codeartifact.types.timestamp

        out["expiration"] = capo_codeartifact.types.timestamp.deserialize_json(
            data["expiration"]
        )
    return out

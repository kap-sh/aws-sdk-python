"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#DeleteConnectionRecordingPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.client_token


class DeleteConnectionRecordingPreferencesResponse(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_guiconnect.types.client_token.ClientToken"]
    """<p>Service-provided idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionRecordingPreferencesResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteConnectionRecordingPreferencesResponse:
    out: DeleteConnectionRecordingPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#GetConnectionRecordingPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.client_token
    import capo_ssm_guiconnect.types.connection_recording_preferences


class GetConnectionRecordingPreferencesResponse(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_guiconnect.types.client_token.ClientToken"]
    """<p>Service-provided idempotency token.</p>"""
    connection_recording_preferences: NotRequired[
        "capo_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences"
    ]
    """<p>The set of preferences used for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region. This includes details such as which S3 bucket recordings are stored in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionRecordingPreferencesResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "connection_recording_preferences" in value:
        import capo_ssm_guiconnect.types.connection_recording_preferences

        out["ConnectionRecordingPreferences"] = (
            capo_ssm_guiconnect.types.connection_recording_preferences.serialize_json(
                value["connection_recording_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConnectionRecordingPreferencesResponse:
    out: GetConnectionRecordingPreferencesResponse = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ConnectionRecordingPreferences" in data:
        import capo_ssm_guiconnect.types.connection_recording_preferences

        out["connection_recording_preferences"] = (
            capo_ssm_guiconnect.types.connection_recording_preferences.deserialize_json(
                data["ConnectionRecordingPreferences"]
            )
        )
    return out

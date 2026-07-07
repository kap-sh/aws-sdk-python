"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#UpdateConnectionRecordingPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_guiconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_guiconnect.types.client_token
    import aws_sdk_ssm_guiconnect.types.connection_recording_preferences


class UpdateConnectionRecordingPreferencesRequest(TypedDict, closed=True):
    connection_recording_preferences: "aws_sdk_ssm_guiconnect.types.connection_recording_preferences.ConnectionRecordingPreferences"
    """<p>The set of preferences used for recording RDP connections in the requesting Amazon Web Services account and Amazon Web Services Region. This includes details such as which S3 bucket recordings are stored in.</p>"""
    client_token: NotRequired["aws_sdk_ssm_guiconnect.types.client_token.ClientToken"]
    """<p>User-provided idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectionRecordingPreferencesRequest) -> dict:
    out: dict = {}
    import aws_sdk_ssm_guiconnect.types.connection_recording_preferences

    out["ConnectionRecordingPreferences"] = (
        aws_sdk_ssm_guiconnect.types.connection_recording_preferences.serialize_json(
            value["connection_recording_preferences"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateConnectionRecordingPreferencesRequest:
    out: UpdateConnectionRecordingPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "ConnectionRecordingPreferences" in data:
        import aws_sdk_ssm_guiconnect.types.connection_recording_preferences

        out["connection_recording_preferences"] = (
            aws_sdk_ssm_guiconnect.types.connection_recording_preferences.deserialize_json(
                data["ConnectionRecordingPreferences"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateConnectionRecordingPreferencesRequest.connection_recording_preferences required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

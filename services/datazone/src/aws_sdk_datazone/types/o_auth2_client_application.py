"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2ClientApplication``."""

from typing import TypedDict

from typing_extensions import NotRequired


class OAuth2ClientApplication(TypedDict):
    user_managed_client_application_client_id: NotRequired["str"]
    """<p>The user managed client application client ID in the OAuth2Client application.</p>"""
    a_ws_managed_client_application_reference: NotRequired["str"]
    """<p>The Amazon Web Services managed client application reference in the OAuth2Client application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2ClientApplication) -> dict:
    out: dict = {}
    if "user_managed_client_application_client_id" in value:
        out["userManagedClientApplicationClientId"] = value[
            "user_managed_client_application_client_id"
        ]
    if "a_ws_managed_client_application_reference" in value:
        out["aWSManagedClientApplicationReference"] = value[
            "a_ws_managed_client_application_reference"
        ]
    return out


def deserialize_json(data: dict) -> OAuth2ClientApplication:
    out: OAuth2ClientApplication = {}  # type: ignore[typeddict-item]
    if "userManagedClientApplicationClientId" in data:
        out["user_managed_client_application_client_id"] = data[
            "userManagedClientApplicationClientId"
        ]
    if "aWSManagedClientApplicationReference" in data:
        out["a_ws_managed_client_application_reference"] = data[
            "aWSManagedClientApplicationReference"
        ]
    return out

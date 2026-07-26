"""Generated from Smithy shape ``com.amazonaws.securityir#IncidentResponder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import capo_security_ir.types.communication_preferences
    import capo_security_ir.types.email_address
    import capo_security_ir.types.incident_responder_name
    import capo_security_ir.types.job_title


class IncidentResponder(TypedDict, closed=True):
    name: "capo_security_ir.types.incident_responder_name.IncidentResponderName"
    """<p/>"""
    job_title: "capo_security_ir.types.job_title.JobTitle"
    """<p/>"""
    email: "capo_security_ir.types.email_address.EmailAddress"
    """<p/>"""
    communication_preferences: NotRequired[
        "capo_security_ir.types.communication_preferences.CommunicationPreferences"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentResponder) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["jobTitle"] = value["job_title"]
    out["email"] = value["email"]
    if "communication_preferences" in value:
        import capo_security_ir.types.communication_preferences

        out["communicationPreferences"] = (
            capo_security_ir.types.communication_preferences.serialize_json(
                value["communication_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> IncidentResponder:
    out: IncidentResponder = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("IncidentResponder.name required")
    if "jobTitle" in data:
        out["job_title"] = data["jobTitle"]
    else:
        raise DeserializationError("IncidentResponder.job_title required")
    if "email" in data:
        out["email"] = data["email"]
    else:
        raise DeserializationError("IncidentResponder.email required")
    if "communicationPreferences" in data:
        import capo_security_ir.types.communication_preferences

        out["communication_preferences"] = (
            capo_security_ir.types.communication_preferences.deserialize_json(
                data["communicationPreferences"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.securityir#IncidentResponder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.communication_preferences
    import aws_sdk_security_ir.types.email_address
    import aws_sdk_security_ir.types.incident_responder_name
    import aws_sdk_security_ir.types.job_title


class IncidentResponder(TypedDict):
    name: "aws_sdk_security_ir.types.incident_responder_name.IncidentResponderName"
    """<p/>"""
    job_title: "aws_sdk_security_ir.types.job_title.JobTitle"
    """<p/>"""
    email: "aws_sdk_security_ir.types.email_address.EmailAddress"
    """<p/>"""
    communication_preferences: NotRequired[
        "aws_sdk_security_ir.types.communication_preferences.CommunicationPreferences"
    ]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentResponder) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["jobTitle"] = value["job_title"]
    out["email"] = value["email"]
    if "communication_preferences" in value:
        import aws_sdk_security_ir.types.communication_preferences

        out["communicationPreferences"] = (
            aws_sdk_security_ir.types.communication_preferences.serialize_json(
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
        import aws_sdk_security_ir.types.communication_preferences

        out["communication_preferences"] = (
            aws_sdk_security_ir.types.communication_preferences.deserialize_json(
                data["communicationPreferences"]
            )
        )
    return out

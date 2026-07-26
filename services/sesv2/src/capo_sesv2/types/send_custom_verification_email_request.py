"""Generated from Smithy shape ``com.amazonaws.sesv2#SendCustomVerificationEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_template_name


class SendCustomVerificationEmailRequest(TypedDict, closed=True):
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address to verify.</p>"""
    template_name: "capo_sesv2.types.email_template_name.EmailTemplateName"
    """<p>The name of the custom verification email template to use when sending the verification email.</p>"""
    configuration_set_name: NotRequired[
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>Name of a configuration set to use when sending the verification email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendCustomVerificationEmailRequest) -> dict:
    out: dict = {}
    out["EmailAddress"] = value["email_address"]
    out["TemplateName"] = value["template_name"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> SendCustomVerificationEmailRequest:
    out: SendCustomVerificationEmailRequest = {}  # type: ignore[typeddict-item]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError(
            "SendCustomVerificationEmailRequest.email_address required"
        )
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    else:
        raise DeserializationError(
            "SendCustomVerificationEmailRequest.template_name required"
        )
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out

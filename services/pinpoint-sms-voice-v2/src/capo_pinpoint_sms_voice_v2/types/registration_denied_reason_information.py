"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationDeniedReasonInformation``."""

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError


class RegistrationDeniedReasonInformation(TypedDict, closed=True):
    reason: "str"
    """<p>The reason a registration was rejected.</p>"""
    short_description: "str"
    """<p>A short description of the rejection reason.</p>"""
    long_description: NotRequired["str"]
    """<p>A long description of the rejection reason.</p>"""
    documentation_title: NotRequired["str"]
    """<p>The title of the document.</p>"""
    documentation_link: NotRequired["str"]
    """<p>The link to the document.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationDeniedReasonInformation) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    out["ShortDescription"] = value["short_description"]
    if "long_description" in value:
        out["LongDescription"] = value["long_description"]
    if "documentation_title" in value:
        out["DocumentationTitle"] = value["documentation_title"]
    if "documentation_link" in value:
        out["DocumentationLink"] = value["documentation_link"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationDeniedReasonInformation:
    out: RegistrationDeniedReasonInformation = {}  # type: ignore[typeddict-item]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError(
            "RegistrationDeniedReasonInformation.reason required"
        )
    if "ShortDescription" in data:
        out["short_description"] = data["ShortDescription"]
    else:
        raise DeserializationError(
            "RegistrationDeniedReasonInformation.short_description required"
        )
    if "LongDescription" in data:
        out["long_description"] = data["LongDescription"]
    if "DocumentationTitle" in data:
        out["documentation_title"] = data["DocumentationTitle"]
    if "DocumentationLink" in data:
        out["documentation_link"] = data["DocumentationLink"]
    return out

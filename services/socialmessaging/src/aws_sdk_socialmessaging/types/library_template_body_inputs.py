"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LibraryTemplateBodyInputs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.add_contact_number
    import aws_sdk_socialmessaging.types.add_learn_more_link
    import aws_sdk_socialmessaging.types.add_security_recommendation
    import aws_sdk_socialmessaging.types.add_track_package_link
    import aws_sdk_socialmessaging.types.code_expiration_minutes


class LibraryTemplateBodyInputs(TypedDict):
    add_contact_number: NotRequired[
        "aws_sdk_socialmessaging.types.add_contact_number.AddContactNumber"
    ]
    """<p>When true, includes a contact number in the template body.</p>"""
    add_learn_more_link: NotRequired[
        "aws_sdk_socialmessaging.types.add_learn_more_link.AddLearnMoreLink"
    ]
    """<p>When true, includes a \"learn more\" link in the template body.</p>"""
    add_security_recommendation: NotRequired[
        "aws_sdk_socialmessaging.types.add_security_recommendation.AddSecurityRecommendation"
    ]
    """<p>When true, includes security recommendations in the template body.</p>"""
    add_track_package_link: NotRequired[
        "aws_sdk_socialmessaging.types.add_track_package_link.AddTrackPackageLink"
    ]
    """<p>When true, includes a package tracking link in the template body.</p>"""
    code_expiration_minutes: NotRequired[
        "aws_sdk_socialmessaging.types.code_expiration_minutes.CodeExpirationMinutes"
    ]
    """<p>The number of minutes until a verification code or OTP expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LibraryTemplateBodyInputs) -> dict:
    out: dict = {}
    if "add_contact_number" in value:
        out["addContactNumber"] = value["add_contact_number"]
    if "add_learn_more_link" in value:
        out["addLearnMoreLink"] = value["add_learn_more_link"]
    if "add_security_recommendation" in value:
        out["addSecurityRecommendation"] = value["add_security_recommendation"]
    if "add_track_package_link" in value:
        out["addTrackPackageLink"] = value["add_track_package_link"]
    if "code_expiration_minutes" in value:
        out["codeExpirationMinutes"] = value["code_expiration_minutes"]
    return out


def deserialize_json(data: dict) -> LibraryTemplateBodyInputs:
    out: LibraryTemplateBodyInputs = {}  # type: ignore[typeddict-item]
    if "addContactNumber" in data:
        out["add_contact_number"] = data["addContactNumber"]
    if "addLearnMoreLink" in data:
        out["add_learn_more_link"] = data["addLearnMoreLink"]
    if "addSecurityRecommendation" in data:
        out["add_security_recommendation"] = data["addSecurityRecommendation"]
    if "addTrackPackageLink" in data:
        out["add_track_package_link"] = data["addTrackPackageLink"]
    if "codeExpirationMinutes" in data:
        out["code_expiration_minutes"] = data["codeExpirationMinutes"]
    return out

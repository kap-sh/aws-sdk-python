"""Generated from Smithy shape ``com.amazonaws.b2bi#UpdateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.business_name
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.profile_name


class UpdateProfileRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile.</p>"""
    name: NotRequired["aws_sdk_b2bi.types.profile_name.ProfileName"]
    """<p>The name of the profile, used to identify it.</p>"""
    email: NotRequired["aws_sdk_b2bi.types.email.Email"]
    """<p>Specifies the email address associated with this customer profile.</p>"""
    phone: NotRequired["aws_sdk_b2bi.types.phone.Phone"]
    """<p>Specifies the phone number associated with the profile.</p>"""
    business_name: NotRequired["aws_sdk_b2bi.types.business_name.BusinessName"]
    """<p>Specifies the name for the business associated with this profile.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
    if "business_name" in value:
        out["businessName"] = value["business_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProfileRequest:
    out: UpdateProfileRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "email" in data:
        out["email"] = data["email"]
    if "phone" in data:
        out["phone"] = data["phone"]
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    return out

"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import capo_b2bi.types.business_name
    import capo_b2bi.types.email
    import capo_b2bi.types.logging
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_name
    import capo_b2bi.types.tag_list


class CreateProfileRequest(TypedDict, closed=True):
    name: "capo_b2bi.types.profile_name.ProfileName"
    """<p>Specifies the name of the profile.</p>"""
    email: NotRequired["capo_b2bi.types.email.Email"]
    """<p>Specifies the email address associated with this customer profile.</p>"""
    phone: "capo_b2bi.types.phone.Phone"
    """<p>Specifies the phone number associated with the profile.</p>"""
    business_name: "capo_b2bi.types.business_name.BusinessName"
    """<p>Specifies the name for the business associated with this profile.</p>"""
    logging: "capo_b2bi.types.logging.Logging"
    """<p>Specifies whether or not logging is enabled for this profile.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""
    tags: NotRequired["capo_b2bi.types.tag_list.TagList"]
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    out["phone"] = value["phone"]
    out["businessName"] = value["business_name"]
    import capo_b2bi.types.logging

    out["logging"] = capo_b2bi.types.logging.serialize_aws_json_1_0(value["logging"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_b2bi.types.tag_list

        out["tags"] = capo_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateProfileRequest.name required")
    if "email" in data:
        out["email"] = data["email"]
    if "phone" in data:
        out["phone"] = data["phone"]
    else:
        raise DeserializationError("CreateProfileRequest.phone required")
    if "businessName" in data:
        out["business_name"] = data["businessName"]
    else:
        raise DeserializationError("CreateProfileRequest.business_name required")
    if "logging" in data:
        import capo_b2bi.types.logging

        out["logging"] = capo_b2bi.types.logging.deserialize_aws_json_1_0(
            data["logging"]
        )
    else:
        raise DeserializationError("CreateProfileRequest.logging required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import capo_b2bi.types.tag_list

        out["tags"] = capo_b2bi.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.b2bi#CreatePartnershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_options
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.partner_name
    import aws_sdk_b2bi.types.partnership_capabilities
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.tag_list


class CreatePartnershipRequest(TypedDict, closed=True):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    name: "aws_sdk_b2bi.types.partner_name.PartnerName"
    """<p>Specifies a descriptive name for the partnership.</p>"""
    email: "aws_sdk_b2bi.types.email.Email"
    """<p>Specifies the email address associated with this trading partner.</p>"""
    phone: NotRequired["aws_sdk_b2bi.types.phone.Phone"]
    """<p>Specifies the phone number associated with the partnership.</p>"""
    capabilities: "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    """<p>Specifies a list of the capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
    ]
    """<p>Specify the structure that contains the details for the associated capabilities.</p>"""
    client_token: NotRequired["str"]
    """<p>Reserved for future use.</p>"""
    tags: NotRequired["aws_sdk_b2bi.types.tag_list.TagList"]
    """<p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePartnershipRequest) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["name"] = value["name"]
    out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
    import aws_sdk_b2bi.types.partnership_capabilities

    out["capabilities"] = (
        aws_sdk_b2bi.types.partnership_capabilities.serialize_aws_json_1_0(
            value["capabilities"]
        )
    )
    if "capability_options" in value:
        import aws_sdk_b2bi.types.capability_options

        out["capabilityOptions"] = (
            aws_sdk_b2bi.types.capability_options.serialize_aws_json_1_0(
                value["capability_options"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePartnershipRequest:
    out: CreatePartnershipRequest = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("CreatePartnershipRequest.profile_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePartnershipRequest.name required")
    if "email" in data:
        out["email"] = data["email"]
    else:
        raise DeserializationError("CreatePartnershipRequest.email required")
    if "phone" in data:
        out["phone"] = data["phone"]
    if "capabilities" in data:
        import aws_sdk_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            aws_sdk_b2bi.types.partnership_capabilities.deserialize_aws_json_1_0(
                data["capabilities"]
            )
        )
    else:
        raise DeserializationError("CreatePartnershipRequest.capabilities required")
    if "capabilityOptions" in data:
        import aws_sdk_b2bi.types.capability_options

        out["capability_options"] = (
            aws_sdk_b2bi.types.capability_options.deserialize_aws_json_1_0(
                data["capabilityOptions"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_b2bi.types.tag_list

        out["tags"] = aws_sdk_b2bi.types.tag_list.deserialize_aws_json_1_0(data["tags"])
    return out

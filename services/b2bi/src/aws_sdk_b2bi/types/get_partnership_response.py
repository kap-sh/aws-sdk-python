"""Generated from Smithy shape ``com.amazonaws.b2bi#GetPartnershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.capability_options
    import aws_sdk_b2bi.types.created_date
    import aws_sdk_b2bi.types.email
    import aws_sdk_b2bi.types.modified_date
    import aws_sdk_b2bi.types.partner_name
    import aws_sdk_b2bi.types.partnership_capabilities
    import aws_sdk_b2bi.types.partnership_id
    import aws_sdk_b2bi.types.phone
    import aws_sdk_b2bi.types.profile_id
    import aws_sdk_b2bi.types.resource_arn
    import aws_sdk_b2bi.types.trading_partner_id


class GetPartnershipResponse(TypedDict, closed=True):
    profile_id: "aws_sdk_b2bi.types.profile_id.ProfileId"
    """<p>Returns the unique, system-generated identifier for the profile connected to this partnership.</p>"""
    partnership_id: "aws_sdk_b2bi.types.partnership_id.PartnershipId"
    """<p>Returns the unique, system-generated identifier for a partnership.</p>"""
    partnership_arn: "aws_sdk_b2bi.types.resource_arn.ResourceArn"
    """<p>Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>"""
    name: NotRequired["aws_sdk_b2bi.types.partner_name.PartnerName"]
    """<p>Returns the display name of the partnership</p>"""
    email: NotRequired["aws_sdk_b2bi.types.email.Email"]
    """<p>Returns the email address associated with this trading partner.</p>"""
    phone: NotRequired["aws_sdk_b2bi.types.phone.Phone"]
    """<p>Returns the phone number associated with the partnership.</p>"""
    capabilities: NotRequired[
        "aws_sdk_b2bi.types.partnership_capabilities.PartnershipCapabilities"
    ]
    """<p>Returns one or more capabilities associated with this partnership.</p>"""
    capability_options: NotRequired[
        "aws_sdk_b2bi.types.capability_options.CapabilityOptions"
    ]
    trading_partner_id: NotRequired[
        "aws_sdk_b2bi.types.trading_partner_id.TradingPartnerId"
    ]
    """<p>Returns the unique identifier for the partner for this partnership.</p>"""
    created_at: "aws_sdk_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp for creation date and time of the partnership.</p>"""
    modified_at: NotRequired["aws_sdk_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp that identifies the most recent date and time that the partnership was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPartnershipResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["partnershipId"] = value["partnership_id"]
    out["partnershipArn"] = value["partnership_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    if "phone" in value:
        out["phone"] = value["phone"]
    if "capabilities" in value:
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
    if "trading_partner_id" in value:
        out["tradingPartnerId"] = value["trading_partner_id"]
    import aws_sdk_b2bi.types.created_date

    out["createdAt"] = aws_sdk_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import aws_sdk_b2bi.types.modified_date

        out["modifiedAt"] = aws_sdk_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPartnershipResponse:
    out: GetPartnershipResponse = {}  # type: ignore[typeddict-item]
    if "profileId" in data:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("GetPartnershipResponse.profile_id required")
    if "partnershipId" in data:
        out["partnership_id"] = data["partnershipId"]
    else:
        raise DeserializationError("GetPartnershipResponse.partnership_id required")
    if "partnershipArn" in data:
        out["partnership_arn"] = data["partnershipArn"]
    else:
        raise DeserializationError("GetPartnershipResponse.partnership_arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "email" in data:
        out["email"] = data["email"]
    if "phone" in data:
        out["phone"] = data["phone"]
    if "capabilities" in data:
        import aws_sdk_b2bi.types.partnership_capabilities

        out["capabilities"] = (
            aws_sdk_b2bi.types.partnership_capabilities.deserialize_aws_json_1_0(
                data["capabilities"]
            )
        )
    if "capabilityOptions" in data:
        import aws_sdk_b2bi.types.capability_options

        out["capability_options"] = (
            aws_sdk_b2bi.types.capability_options.deserialize_aws_json_1_0(
                data["capabilityOptions"]
            )
        )
    if "tradingPartnerId" in data:
        out["trading_partner_id"] = data["tradingPartnerId"]
    if "createdAt" in data:
        import aws_sdk_b2bi.types.created_date

        out["created_at"] = aws_sdk_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetPartnershipResponse.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_b2bi.types.modified_date

        out["modified_at"] = aws_sdk_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    return out

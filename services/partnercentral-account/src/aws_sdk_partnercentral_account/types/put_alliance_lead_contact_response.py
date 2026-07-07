"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PutAllianceLeadContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.alliance_lead_contact
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.partner_arn
    import aws_sdk_partnercentral_account.types.partner_id


class PutAllianceLeadContactResponse(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "aws_sdk_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "aws_sdk_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    alliance_lead_contact: (
        "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The updated alliance lead contact information.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAllianceLeadContactResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import aws_sdk_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        aws_sdk_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAllianceLeadContactResponse:
    out: PutAllianceLeadContactResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("PutAllianceLeadContactResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("PutAllianceLeadContactResponse.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("PutAllianceLeadContactResponse.id required")
    if "AllianceLeadContact" in data:
        import aws_sdk_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            aws_sdk_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "PutAllianceLeadContactResponse.alliance_lead_contact required"
        )
    return out

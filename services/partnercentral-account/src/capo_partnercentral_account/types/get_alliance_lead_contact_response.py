"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetAllianceLeadContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.alliance_lead_contact
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_arn
    import capo_partnercentral_account.types.partner_id


class GetAllianceLeadContactResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    arn: "capo_partnercentral_account.types.partner_arn.PartnerArn"
    """<p>The Amazon Resource Name (ARN) of the partner account.</p>"""
    id: "capo_partnercentral_account.types.partner_id.PartnerId"
    """<p>The unique identifier of the partner account.</p>"""
    alliance_lead_contact: (
        "capo_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The alliance lead contact information including name, email, and business title.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAllianceLeadContactResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    import capo_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        capo_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAllianceLeadContactResponse:
    out: GetAllianceLeadContactResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetAllianceLeadContactResponse.catalog required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetAllianceLeadContactResponse.arn required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetAllianceLeadContactResponse.id required")
    if "AllianceLeadContact" in data:
        import capo_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            capo_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "GetAllianceLeadContactResponse.alliance_lead_contact required"
        )
    return out

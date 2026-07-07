"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PutAllianceLeadContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.alliance_lead_contact
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.email_verification_code
    import aws_sdk_partnercentral_account.types.partner_identifier


class PutAllianceLeadContactRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: (
        "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    )
    """<p>The unique identifier of the partner account.</p>"""
    alliance_lead_contact: (
        "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The alliance lead contact information to set for the partner account.</p>"""
    email_verification_code: NotRequired[
        "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    ]
    """<p>The verification code sent to the alliance lead contact's email to confirm the update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutAllianceLeadContactRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import aws_sdk_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        aws_sdk_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    if "email_verification_code" in value:
        out["EmailVerificationCode"] = value["email_verification_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutAllianceLeadContactRequest:
    out: PutAllianceLeadContactRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("PutAllianceLeadContactRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("PutAllianceLeadContactRequest.identifier required")
    if "AllianceLeadContact" in data:
        import aws_sdk_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            aws_sdk_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "PutAllianceLeadContactRequest.alliance_lead_contact required"
        )
    if "EmailVerificationCode" in data:
        out["email_verification_code"] = data["EmailVerificationCode"]
    return out

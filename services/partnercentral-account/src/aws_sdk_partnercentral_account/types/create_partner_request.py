"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CreatePartnerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.alliance_lead_contact
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.email_verification_code
    import aws_sdk_partnercentral_account.types.primary_solution_type
    import aws_sdk_partnercentral_account.types.sensitive_unicode_string
    import aws_sdk_partnercentral_account.types.tag_list


class CreatePartnerRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the partner account will be created.</p>"""
    client_token: NotRequired[
        "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    legal_name: "aws_sdk_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The legal name of the organization becoming a partner.</p>"""
    primary_solution_type: (
        "aws_sdk_partnercentral_account.types.primary_solution_type.PrimarySolutionType"
    )
    """<p>The primary type of solution or service the partner provides (e.g., consulting, software, managed services).</p>"""
    alliance_lead_contact: (
        "aws_sdk_partnercentral_account.types.alliance_lead_contact.AllianceLeadContact"
    )
    """<p>The primary contact person for alliance and partnership matters.</p>"""
    email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    """<p>The verification code sent to the alliance lead contact's email to confirm account creation.</p>"""
    tags: NotRequired["aws_sdk_partnercentral_account.types.tag_list.TagList"]
    """<p>A list of tags to associate with the partner account for organization and billing purposes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreatePartnerRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["LegalName"] = value["legal_name"]
    import aws_sdk_partnercentral_account.types.primary_solution_type

    out["PrimarySolutionType"] = (
        aws_sdk_partnercentral_account.types.primary_solution_type.serialize_aws_json_1_0(
            value["primary_solution_type"]
        )
    )
    import aws_sdk_partnercentral_account.types.alliance_lead_contact

    out["AllianceLeadContact"] = (
        aws_sdk_partnercentral_account.types.alliance_lead_contact.serialize_aws_json_1_0(
            value["alliance_lead_contact"]
        )
    )
    out["EmailVerificationCode"] = value["email_verification_code"]
    if "tags" in value:
        import aws_sdk_partnercentral_account.types.tag_list

        out["Tags"] = (
            aws_sdk_partnercentral_account.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreatePartnerRequest:
    out: CreatePartnerRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreatePartnerRequest.catalog required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "LegalName" in data:
        out["legal_name"] = data["LegalName"]
    else:
        raise DeserializationError("CreatePartnerRequest.legal_name required")
    if "PrimarySolutionType" in data:
        import aws_sdk_partnercentral_account.types.primary_solution_type

        out["primary_solution_type"] = (
            aws_sdk_partnercentral_account.types.primary_solution_type.deserialize_aws_json_1_0(
                data["PrimarySolutionType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePartnerRequest.primary_solution_type required"
        )
    if "AllianceLeadContact" in data:
        import aws_sdk_partnercentral_account.types.alliance_lead_contact

        out["alliance_lead_contact"] = (
            aws_sdk_partnercentral_account.types.alliance_lead_contact.deserialize_aws_json_1_0(
                data["AllianceLeadContact"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePartnerRequest.alliance_lead_contact required"
        )
    if "EmailVerificationCode" in data:
        out["email_verification_code"] = data["EmailVerificationCode"]
    else:
        raise DeserializationError(
            "CreatePartnerRequest.email_verification_code required"
        )
    if "Tags" in data:
        import aws_sdk_partnercentral_account.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_account.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out

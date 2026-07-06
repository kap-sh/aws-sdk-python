"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#AssociateAwsTrainingCertificationEmailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.email
    import aws_sdk_partnercentral_account.types.email_verification_code
    import aws_sdk_partnercentral_account.types.partner_identifier


class AssociateAwsTrainingCertificationEmailDomainRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: (
        "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    )
    """<p>The unique identifier of the partner account.</p>"""
    client_token: NotRequired[
        "aws_sdk_partnercentral_account.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    email: "aws_sdk_partnercentral_account.types.email.Email"
    """<p>The email address used to verify domain ownership for AWS training and certification association.</p>"""
    email_verification_code: "aws_sdk_partnercentral_account.types.email_verification_code.EmailVerificationCode"
    """<p>The verification code sent to the email address to confirm domain ownership.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: AssociateAwsTrainingCertificationEmailDomainRequest,
) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Email"] = value["email"]
    out["EmailVerificationCode"] = value["email_verification_code"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> AssociateAwsTrainingCertificationEmailDomainRequest:
    out: AssociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.catalog required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.identifier required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "Email" in data:
        out["email"] = data["Email"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.email required"
        )
    if "EmailVerificationCode" in data:
        out["email_verification_code"] = data["EmailVerificationCode"]
    else:
        raise DeserializationError(
            "AssociateAwsTrainingCertificationEmailDomainRequest.email_verification_code required"
        )
    return out

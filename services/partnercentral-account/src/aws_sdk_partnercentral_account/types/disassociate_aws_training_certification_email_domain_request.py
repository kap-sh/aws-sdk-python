"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#DisassociateAwsTrainingCertificationEmailDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.client_token
    import aws_sdk_partnercentral_account.types.domain_name
    import aws_sdk_partnercentral_account.types.partner_identifier


class DisassociateAwsTrainingCertificationEmailDomainRequest(TypedDict, closed=True):
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
    domain_name: "aws_sdk_partnercentral_account.types.domain_name.DomainName"
    """<p>The domain name to disassociate from AWS training and certification.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: DisassociateAwsTrainingCertificationEmailDomainRequest,
) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> DisassociateAwsTrainingCertificationEmailDomainRequest:
    out: DisassociateAwsTrainingCertificationEmailDomainRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "DisassociateAwsTrainingCertificationEmailDomainRequest.catalog required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "DisassociateAwsTrainingCertificationEmailDomainRequest.identifier required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError(
            "DisassociateAwsTrainingCertificationEmailDomainRequest.domain_name required"
        )
    return out

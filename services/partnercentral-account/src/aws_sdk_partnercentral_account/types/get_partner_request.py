"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetPartnerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.partner_identifier


class GetPartnerRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: (
        "aws_sdk_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    )
    """<p>The unique identifier of the partner account to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPartnerRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPartnerRequest:
    out: GetPartnerRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetPartnerRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetPartnerRequest.identifier required")
    return out

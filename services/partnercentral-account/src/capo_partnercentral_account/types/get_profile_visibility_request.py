"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetProfileVisibilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.partner_identifier


class GetProfileVisibilityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    identifier: "capo_partnercentral_account.types.partner_identifier.PartnerIdentifier"
    """<p>The unique identifier of the partner account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProfileVisibilityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProfileVisibilityRequest:
    out: GetProfileVisibilityRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetProfileVisibilityRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("GetProfileVisibilityRequest.identifier required")
    return out

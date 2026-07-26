"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.partner_profile_id
    import capo_partnercentral_account.types.unicode_string


class PartnerProfileSummary(TypedDict, closed=True):
    id: "capo_partnercentral_account.types.partner_profile_id.PartnerProfileId"
    """<p>The unique identifier of the partner profile.</p>"""
    name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The display name of the partner.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerProfileSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PartnerProfileSummary:
    out: PartnerProfileSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("PartnerProfileSummary.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PartnerProfileSummary.name required")
    return out

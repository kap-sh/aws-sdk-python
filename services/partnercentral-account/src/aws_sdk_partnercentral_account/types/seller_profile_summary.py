"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#SellerProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.seller_profile_id
    import aws_sdk_partnercentral_account.types.unicode_string


class SellerProfileSummary(TypedDict, closed=True):
    id: "aws_sdk_partnercentral_account.types.seller_profile_id.SellerProfileId"
    """<p>The unique identifier of the seller profile.</p>"""
    name: "aws_sdk_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The display name of the seller.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SellerProfileSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SellerProfileSummary:
    out: SellerProfileSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SellerProfileSummary.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SellerProfileSummary.name required")
    return out

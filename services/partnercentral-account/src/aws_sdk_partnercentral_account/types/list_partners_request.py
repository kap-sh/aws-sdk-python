"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListPartnersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog
    import aws_sdk_partnercentral_account.types.next_token


class ListPartnersRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier to list partners from.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results in paginated responses.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPartnersRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPartnersRequest:
    out: ListPartnersRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListPartnersRequest.catalog required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

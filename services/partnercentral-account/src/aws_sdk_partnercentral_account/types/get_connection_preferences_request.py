"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetConnectionPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.catalog


class GetConnectionPreferencesRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionPreferencesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionPreferencesRequest:
    out: GetConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetConnectionPreferencesRequest.catalog required")
    return out

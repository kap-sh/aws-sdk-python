"""Generated from Smithy shape ``com.amazonaws.glue#GetCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string


class GetCatalogRequest(TypedDict, closed=True):
    catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the parent catalog in which the catalog resides. If none is provided, the Amazon Web Services Account Number is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCatalogRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCatalogRequest:
    out: GetCatalogRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("GetCatalogRequest.catalog_id required")
    return out

"""Generated from Smithy shape ``com.amazonaws.glue#DeleteCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string


class DeleteCatalogRequest(TypedDict, closed=True):
    catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
    """<p>The ID of the catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCatalogRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCatalogRequest:
    out: DeleteCatalogRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("DeleteCatalogRequest.catalog_id required")
    return out

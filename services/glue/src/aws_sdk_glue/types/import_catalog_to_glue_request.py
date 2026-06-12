"""Generated from Smithy shape ``com.amazonaws.glue#ImportCatalogToGlueRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string


class ImportCatalogToGlueRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog to import. Currently, this should be the Amazon Web Services account ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCatalogToGlueRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCatalogToGlueRequest:
    out: ImportCatalogToGlueRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out

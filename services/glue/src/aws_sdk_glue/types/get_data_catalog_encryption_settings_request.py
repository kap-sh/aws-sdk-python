"""Generated from Smithy shape ``com.amazonaws.glue#GetDataCatalogEncryptionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string


class GetDataCatalogEncryptionSettingsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog to retrieve the security configuration for. If none is provided, the Amazon Web Services account ID is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataCatalogEncryptionSettingsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataCatalogEncryptionSettingsRequest:
    out: GetDataCatalogEncryptionSettingsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out

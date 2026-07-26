"""Generated from Smithy shape ``com.amazonaws.glue#PutDataCatalogEncryptionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.data_catalog_encryption_settings


class PutDataCatalogEncryptionSettingsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog to set the security configuration for. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    data_catalog_encryption_settings: (
        "capo_glue.types.data_catalog_encryption_settings.DataCatalogEncryptionSettings"
    )
    """<p>The security configuration to set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutDataCatalogEncryptionSettingsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_glue.types.data_catalog_encryption_settings

    out["DataCatalogEncryptionSettings"] = (
        capo_glue.types.data_catalog_encryption_settings.serialize_aws_json_1_1(
            value["data_catalog_encryption_settings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutDataCatalogEncryptionSettingsRequest:
    out: PutDataCatalogEncryptionSettingsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DataCatalogEncryptionSettings" in data:
        import capo_glue.types.data_catalog_encryption_settings

        out["data_catalog_encryption_settings"] = (
            capo_glue.types.data_catalog_encryption_settings.deserialize_aws_json_1_1(
                data["DataCatalogEncryptionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "PutDataCatalogEncryptionSettingsRequest.data_catalog_encryption_settings required"
        )
    return out

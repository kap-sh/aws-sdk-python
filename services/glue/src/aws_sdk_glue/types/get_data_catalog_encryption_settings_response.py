"""Generated from Smithy shape ``com.amazonaws.glue#GetDataCatalogEncryptionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_catalog_encryption_settings


class GetDataCatalogEncryptionSettingsResponse(TypedDict, closed=True):
    data_catalog_encryption_settings: NotRequired[
        "aws_sdk_glue.types.data_catalog_encryption_settings.DataCatalogEncryptionSettings"
    ]
    """<p>The requested security configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataCatalogEncryptionSettingsResponse) -> dict:
    out: dict = {}
    if "data_catalog_encryption_settings" in value:
        import aws_sdk_glue.types.data_catalog_encryption_settings

        out["DataCatalogEncryptionSettings"] = (
            aws_sdk_glue.types.data_catalog_encryption_settings.serialize_aws_json_1_1(
                value["data_catalog_encryption_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataCatalogEncryptionSettingsResponse:
    out: GetDataCatalogEncryptionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "DataCatalogEncryptionSettings" in data:
        import aws_sdk_glue.types.data_catalog_encryption_settings

        out["data_catalog_encryption_settings"] = (
            aws_sdk_glue.types.data_catalog_encryption_settings.deserialize_aws_json_1_1(
                data["DataCatalogEncryptionSettings"]
            )
        )
    return out

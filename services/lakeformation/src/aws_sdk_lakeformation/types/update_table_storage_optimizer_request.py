"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateTableStorageOptimizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string
    import aws_sdk_lakeformation.types.storage_optimizer_config_map


class UpdateTableStorageOptimizerRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The Catalog ID of the table.</p>"""
    database_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>Name of the database where the table is present.</p>"""
    table_name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>Name of the table for which to enable the storage optimizer.</p>"""
    storage_optimizer_config: "aws_sdk_lakeformation.types.storage_optimizer_config_map.StorageOptimizerConfigMap"
    """<p>Name of the configuration for the storage optimizer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableStorageOptimizerRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_lakeformation.types.storage_optimizer_config_map

    out["StorageOptimizerConfig"] = (
        aws_sdk_lakeformation.types.storage_optimizer_config_map.serialize_json(
            value["storage_optimizer_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTableStorageOptimizerRequest:
    out: UpdateTableStorageOptimizerRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "UpdateTableStorageOptimizerRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateTableStorageOptimizerRequest.table_name required"
        )
    if "StorageOptimizerConfig" in data:
        import aws_sdk_lakeformation.types.storage_optimizer_config_map

        out["storage_optimizer_config"] = (
            aws_sdk_lakeformation.types.storage_optimizer_config_map.deserialize_json(
                data["StorageOptimizerConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTableStorageOptimizerRequest.storage_optimizer_config required"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.firehose#CatalogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.glue_data_catalog_arn
    import capo_firehose.types.warehouse_location


class CatalogConfiguration(TypedDict, closed=True):
    catalog_arn: NotRequired[
        "capo_firehose.types.glue_data_catalog_arn.GlueDataCatalogARN"
    ]
    """<p> Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables. You must specify the ARN in the format <code>arn:aws:glue:region:account-id:catalog</code>. </p>"""
    warehouse_location: NotRequired[
        "capo_firehose.types.warehouse_location.WarehouseLocation"
    ]
    """<p>The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled.</p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogConfiguration) -> dict:
    out: dict = {}
    if "catalog_arn" in value:
        out["CatalogARN"] = value["catalog_arn"]
    if "warehouse_location" in value:
        out["WarehouseLocation"] = value["warehouse_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogConfiguration:
    out: CatalogConfiguration = {}  # type: ignore[typeddict-item]
    if "CatalogARN" in data:
        out["catalog_arn"] = data["CatalogARN"]
    if "WarehouseLocation" in data:
        out["warehouse_location"] = data["WarehouseLocation"]
    return out

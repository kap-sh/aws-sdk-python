"""Generated from Smithy shape ``com.amazonaws.glue#CatalogProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_lake_access_properties
    import aws_sdk_glue.types.iceberg_optimization_properties
    import aws_sdk_glue.types.parameters_map


class CatalogProperties(TypedDict):
    data_lake_access_properties: NotRequired[
        "aws_sdk_glue.types.data_lake_access_properties.DataLakeAccessProperties"
    ]
    """<p>A <code>DataLakeAccessProperties</code> object that specifies properties to configure data lake access for your catalog resource in the Glue Data Catalog.</p>"""
    iceberg_optimization_properties: NotRequired[
        "aws_sdk_glue.types.iceberg_optimization_properties.IcebergOptimizationProperties"
    ]
    """<p>A structure that specifies Iceberg table optimization properties for the catalog. This includes configuration for compaction, retention, and orphan file deletion operations that can be applied to Iceberg tables in this catalog.</p>"""
    custom_properties: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>Additional key-value properties for the catalog, such as column statistics optimizations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogProperties) -> dict:
    out: dict = {}
    if "data_lake_access_properties" in value:
        import aws_sdk_glue.types.data_lake_access_properties

        out["DataLakeAccessProperties"] = (
            aws_sdk_glue.types.data_lake_access_properties.serialize_aws_json_1_1(
                value["data_lake_access_properties"]
            )
        )
    if "iceberg_optimization_properties" in value:
        import aws_sdk_glue.types.iceberg_optimization_properties

        out["IcebergOptimizationProperties"] = (
            aws_sdk_glue.types.iceberg_optimization_properties.serialize_aws_json_1_1(
                value["iceberg_optimization_properties"]
            )
        )
    if "custom_properties" in value:
        import aws_sdk_glue.types.parameters_map

        out["CustomProperties"] = (
            aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
                value["custom_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogProperties:
    out: CatalogProperties = {}  # type: ignore[typeddict-item]
    if "DataLakeAccessProperties" in data:
        import aws_sdk_glue.types.data_lake_access_properties

        out["data_lake_access_properties"] = (
            aws_sdk_glue.types.data_lake_access_properties.deserialize_aws_json_1_1(
                data["DataLakeAccessProperties"]
            )
        )
    if "IcebergOptimizationProperties" in data:
        import aws_sdk_glue.types.iceberg_optimization_properties

        out["iceberg_optimization_properties"] = (
            aws_sdk_glue.types.iceberg_optimization_properties.deserialize_aws_json_1_1(
                data["IcebergOptimizationProperties"]
            )
        )
    if "CustomProperties" in data:
        import aws_sdk_glue.types.parameters_map

        out["custom_properties"] = (
            aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
                data["CustomProperties"]
            )
        )
    return out

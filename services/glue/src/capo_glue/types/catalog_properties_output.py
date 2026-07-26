"""Generated from Smithy shape ``com.amazonaws.glue#CatalogPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_lake_access_properties_output
    import capo_glue.types.iceberg_optimization_properties_output
    import capo_glue.types.parameters_map


class CatalogPropertiesOutput(TypedDict, closed=True):
    data_lake_access_properties: NotRequired[
        "capo_glue.types.data_lake_access_properties_output.DataLakeAccessPropertiesOutput"
    ]
    """<p>A <code>DataLakeAccessProperties</code> object with input properties to configure data lake access for your catalog resource in the Glue Data Catalog.</p>"""
    iceberg_optimization_properties: NotRequired[
        "capo_glue.types.iceberg_optimization_properties_output.IcebergOptimizationPropertiesOutput"
    ]
    """<p>An <code>IcebergOptimizationPropertiesOutput</code> object that specifies Iceberg table optimization settings for the catalog, including configurations for compaction, retention, and orphan file deletion operations.</p>"""
    custom_properties: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>Additional key-value properties for the catalog, such as column statistics optimizations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogPropertiesOutput) -> dict:
    out: dict = {}
    if "data_lake_access_properties" in value:
        import capo_glue.types.data_lake_access_properties_output

        out["DataLakeAccessProperties"] = (
            capo_glue.types.data_lake_access_properties_output.serialize_aws_json_1_1(
                value["data_lake_access_properties"]
            )
        )
    if "iceberg_optimization_properties" in value:
        import capo_glue.types.iceberg_optimization_properties_output

        out["IcebergOptimizationProperties"] = (
            capo_glue.types.iceberg_optimization_properties_output.serialize_aws_json_1_1(
                value["iceberg_optimization_properties"]
            )
        )
    if "custom_properties" in value:
        import capo_glue.types.parameters_map

        out["CustomProperties"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["custom_properties"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogPropertiesOutput:
    out: CatalogPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "DataLakeAccessProperties" in data:
        import capo_glue.types.data_lake_access_properties_output

        out["data_lake_access_properties"] = (
            capo_glue.types.data_lake_access_properties_output.deserialize_aws_json_1_1(
                data["DataLakeAccessProperties"]
            )
        )
    if "IcebergOptimizationProperties" in data:
        import capo_glue.types.iceberg_optimization_properties_output

        out["iceberg_optimization_properties"] = (
            capo_glue.types.iceberg_optimization_properties_output.deserialize_aws_json_1_1(
                data["IcebergOptimizationProperties"]
            )
        )
    if "CustomProperties" in data:
        import capo_glue.types.parameters_map

        out["custom_properties"] = (
            capo_glue.types.parameters_map.deserialize_aws_json_1_1(
                data["CustomProperties"]
            )
        )
    return out

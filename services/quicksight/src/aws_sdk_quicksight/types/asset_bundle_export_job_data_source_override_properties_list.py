"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSourceOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties

AssetBundleExportJobDataSourceOverridePropertiesList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties.AssetBundleExportJobDataSourceOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSourceOverridePropertiesList) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobDataSourceOverridePropertiesList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties

    out: AssetBundleExportJobDataSourceOverridePropertiesList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_data_source_override_properties.deserialize_json(
                item
            )
        )
    return out

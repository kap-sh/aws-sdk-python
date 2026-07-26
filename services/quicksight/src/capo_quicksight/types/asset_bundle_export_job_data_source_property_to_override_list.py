"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSourcePropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override

AssetBundleExportJobDataSourcePropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override.AssetBundleExportJobDataSourcePropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSourcePropertyToOverrideList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobDataSourcePropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override

    out: AssetBundleExportJobDataSourcePropertyToOverrideList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_source_property_to_override.deserialize_json(
                item
            )
        )
    return out

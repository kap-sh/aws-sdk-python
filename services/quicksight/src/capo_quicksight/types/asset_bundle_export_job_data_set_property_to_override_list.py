"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetPropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override

AssetBundleExportJobDataSetPropertyToOverrideList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override.AssetBundleExportJobDataSetPropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSetPropertyToOverrideList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobDataSetPropertyToOverrideList:
    import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override

    out: AssetBundleExportJobDataSetPropertyToOverrideList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override.deserialize_json(
                item
            )
        )
    return out

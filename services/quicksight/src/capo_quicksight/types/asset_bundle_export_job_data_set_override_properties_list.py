"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_export_job_data_set_override_properties

AssetBundleExportJobDataSetOverridePropertiesList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_export_job_data_set_override_properties.AssetBundleExportJobDataSetOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSetOverridePropertiesList) -> list:
    import capo_quicksight.types.asset_bundle_export_job_data_set_override_properties

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_set_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleExportJobDataSetOverridePropertiesList:
    import capo_quicksight.types.asset_bundle_export_job_data_set_override_properties

    out: AssetBundleExportJobDataSetOverridePropertiesList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_export_job_data_set_override_properties.deserialize_json(
                item
            )
        )
    return out

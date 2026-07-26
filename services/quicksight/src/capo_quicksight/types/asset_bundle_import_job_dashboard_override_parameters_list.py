"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDashboardOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters

AssetBundleImportJobDashboardOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters.AssetBundleImportJobDashboardOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDashboardOverrideParametersList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobDashboardOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters

    out: AssetBundleImportJobDashboardOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_dashboard_override_parameters.deserialize_json(
                item
            )
        )
    return out

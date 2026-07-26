"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobVPCConnectionOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

AssetBundleImportJobVPCConnectionOverrideParametersList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.AssetBundleImportJobVPCConnectionOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobVPCConnectionOverrideParametersList,
) -> list:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobVPCConnectionOverrideParametersList:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

    out: AssetBundleImportJobVPCConnectionOverrideParametersList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobVPCConnectionOverrideParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

AssetBundleImportJobVPCConnectionOverrideParametersList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.AssetBundleImportJobVPCConnectionOverrideParameters"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleImportJobVPCConnectionOverrideParametersList,
) -> list:
    import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleImportJobVPCConnectionOverrideParametersList:
    import aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters

    out: AssetBundleImportJobVPCConnectionOverrideParametersList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_import_job_vpc_connection_override_parameters.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobVPCConnectionOverridePropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties

AssetBundleExportJobVPCConnectionOverridePropertiesList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties.AssetBundleExportJobVPCConnectionOverrideProperties"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobVPCConnectionOverridePropertiesList,
) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobVPCConnectionOverridePropertiesList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties

    out: AssetBundleExportJobVPCConnectionOverridePropertiesList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_override_properties.deserialize_json(
                item
            )
        )
    return out

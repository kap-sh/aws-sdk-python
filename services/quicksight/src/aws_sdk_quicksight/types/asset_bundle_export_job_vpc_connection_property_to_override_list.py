"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobVPCConnectionPropertyToOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override

AssetBundleExportJobVPCConnectionPropertyToOverrideList: TypeAlias = list[
    "aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override.AssetBundleExportJobVPCConnectionPropertyToOverride"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AssetBundleExportJobVPCConnectionPropertyToOverrideList,
) -> list:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AssetBundleExportJobVPCConnectionPropertyToOverrideList:
    import aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override

    out: AssetBundleExportJobVPCConnectionPropertyToOverrideList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.asset_bundle_export_job_vpc_connection_property_to_override.deserialize_json(
                item
            )
        )
    return out

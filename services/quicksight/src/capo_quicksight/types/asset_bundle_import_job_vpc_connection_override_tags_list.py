"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobVPCConnectionOverrideTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags

AssetBundleImportJobVPCConnectionOverrideTagsList: TypeAlias = list[
    "capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags.AssetBundleImportJobVPCConnectionOverrideTags"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobVPCConnectionOverrideTagsList) -> list:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssetBundleImportJobVPCConnectionOverrideTagsList:
    import capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags

    out: AssetBundleImportJobVPCConnectionOverrideTagsList = []
    for item in data:
        out.append(
            capo_quicksight.types.asset_bundle_import_job_vpc_connection_override_tags.deserialize_json(
                item
            )
        )
    return out

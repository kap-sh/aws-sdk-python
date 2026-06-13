"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#DeleteResourceExplorerSetupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.region_list


class DeleteResourceExplorerSetupInput(TypedDict):
    region_list: NotRequired["aws_sdk_resource_explorer_2.types.region_list.RegionList"]
    """<p>A list of Amazon Web Services Regions from which to delete the Resource Explorer configuration. If not specified, the operation uses the <code>DeleteInAllRegions</code> parameter to determine scope.</p>"""
    delete_in_all_regions: NotRequired["bool"]
    """<p>Specifies whether to delete Resource Explorer configuration from all Regions where it is currently enabled. If this parameter is set to <code>true</code>, a value for <code>RegionList</code> must not be provided. Otherwise, the operation fails with a <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceExplorerSetupInput) -> dict:
    out: dict = {}
    if "region_list" in value:
        import aws_sdk_resource_explorer_2.types.region_list

        out["RegionList"] = (
            aws_sdk_resource_explorer_2.types.region_list.serialize_json(
                value["region_list"]
            )
        )
    if "delete_in_all_regions" in value:
        out["DeleteInAllRegions"] = value["delete_in_all_regions"]
    return out


def deserialize_json(data: dict) -> DeleteResourceExplorerSetupInput:
    out: DeleteResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
    if "RegionList" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["region_list"] = (
            aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
                data["RegionList"]
            )
        )
    if "DeleteInAllRegions" in data:
        out["delete_in_all_regions"] = data["DeleteInAllRegions"]
    return out

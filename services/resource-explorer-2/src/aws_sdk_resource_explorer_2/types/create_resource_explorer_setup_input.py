"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateResourceExplorerSetupInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.region_list


class CreateResourceExplorerSetupInput(TypedDict):
    region_list: "aws_sdk_resource_explorer_2.types.region_list.RegionList"
    """<p>A list of Amazon Web Services Regions where Resource Explorer should be configured. Each Region in the list will have a user-owned index created.</p>"""
    aggregator_regions: NotRequired[
        "aws_sdk_resource_explorer_2.types.region_list.RegionList"
    ]
    """<p>A list of Amazon Web Services Regions that should be configured as aggregator Regions. Aggregator Regions receive replicated index information from all other Regions where there is a user-owned index.</p>"""
    view_name: "str"
    """<p>The name for the view to be created as part of the Resource Explorer setup. The view name must be unique within the Amazon Web Services account and Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceExplorerSetupInput) -> dict:
    out: dict = {}
    import aws_sdk_resource_explorer_2.types.region_list

    out["RegionList"] = aws_sdk_resource_explorer_2.types.region_list.serialize_json(
        value["region_list"]
    )
    if "aggregator_regions" in value:
        import aws_sdk_resource_explorer_2.types.region_list

        out["AggregatorRegions"] = (
            aws_sdk_resource_explorer_2.types.region_list.serialize_json(
                value["aggregator_regions"]
            )
        )
    out["ViewName"] = value["view_name"]
    return out


def deserialize_json(data: dict) -> CreateResourceExplorerSetupInput:
    out: CreateResourceExplorerSetupInput = {}  # type: ignore[typeddict-item]
    if "RegionList" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["region_list"] = (
            aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
                data["RegionList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateResourceExplorerSetupInput.region_list required"
        )
    if "AggregatorRegions" in data:
        import aws_sdk_resource_explorer_2.types.region_list

        out["aggregator_regions"] = (
            aws_sdk_resource_explorer_2.types.region_list.deserialize_json(
                data["AggregatorRegions"]
            )
        )
    if "ViewName" in data:
        out["view_name"] = data["ViewName"]
    else:
        raise DeserializationError(
            "CreateResourceExplorerSetupInput.view_name required"
        )
    return out

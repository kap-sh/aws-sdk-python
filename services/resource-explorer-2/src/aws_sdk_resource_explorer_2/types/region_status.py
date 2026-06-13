"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#RegionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.index_status
    import aws_sdk_resource_explorer_2.types.view_status


class RegionStatus(TypedDict):
    region: NotRequired["str"]
    """<p>The Amazon Web Services Region for which this status information applies.</p>"""
    index: NotRequired["aws_sdk_resource_explorer_2.types.index_status.IndexStatus"]
    """<p>The status information for the Resource Explorer index in this Region.</p>"""
    view: NotRequired["aws_sdk_resource_explorer_2.types.view_status.ViewStatus"]
    """<p>The status information for the Resource Explorer view in this Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionStatus) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "index" in value:
        import aws_sdk_resource_explorer_2.types.index_status

        out["Index"] = aws_sdk_resource_explorer_2.types.index_status.serialize_json(
            value["index"]
        )
    if "view" in value:
        import aws_sdk_resource_explorer_2.types.view_status

        out["View"] = aws_sdk_resource_explorer_2.types.view_status.serialize_json(
            value["view"]
        )
    return out


def deserialize_json(data: dict) -> RegionStatus:
    out: RegionStatus = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    if "Index" in data:
        import aws_sdk_resource_explorer_2.types.index_status

        out["index"] = aws_sdk_resource_explorer_2.types.index_status.deserialize_json(
            data["Index"]
        )
    if "View" in data:
        import aws_sdk_resource_explorer_2.types.view_status

        out["view"] = aws_sdk_resource_explorer_2.types.view_status.deserialize_json(
            data["View"]
        )
    return out

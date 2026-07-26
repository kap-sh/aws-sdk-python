"""Generated from Smithy shape ``com.amazonaws.workdocs#DescribeGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.group_metadata_list
    import capo_workdocs.types.marker_type


class DescribeGroupsResponse(TypedDict, closed=True):
    groups: NotRequired["capo_workdocs.types.group_metadata_list.GroupMetadataList"]
    """<p>The list of groups.</p>"""
    marker: NotRequired["capo_workdocs.types.marker_type.MarkerType"]
    """<p>The marker to use when requesting the next set of results. If there are no additional results, the string is empty.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_workdocs.types.group_metadata_list

        out["Groups"] = capo_workdocs.types.group_metadata_list.serialize_json(
            value["groups"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_json(data: dict) -> DescribeGroupsResponse:
    out: DescribeGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_workdocs.types.group_metadata_list

        out["groups"] = capo_workdocs.types.group_metadata_list.deserialize_json(
            data["Groups"]
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out

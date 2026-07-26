"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListConnectionGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.connection_group_summary_list
    import capo_cloudfront.types.string


class ListConnectionGroupsResult(TypedDict, closed=True):
    next_marker: NotRequired["capo_cloudfront.types.string.string"]
    """<p>A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.</p>"""
    connection_groups: NotRequired[
        "capo_cloudfront.types.connection_group_summary_list.ConnectionGroupSummaryList"
    ]
    """<p>The list of connection groups that you retrieved.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListConnectionGroupsResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "next_marker" in value:
        SubElement(el, "NextMarker").text = str(value["next_marker"])
    if "connection_groups" in value:
        import capo_cloudfront.types.connection_group_summary_list

        capo_cloudfront.types.connection_group_summary_list.serialize_xml(
            value["connection_groups"], el, "ConnectionGroups"
        )


def deserialize_xml(el: Element) -> ListConnectionGroupsResult:
    out: ListConnectionGroupsResult = {}  # type: ignore[typeddict-item]
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    child_connection_groups = el.find("ConnectionGroups")
    if child_connection_groups is not None:
        import capo_cloudfront.types.connection_group_summary_list

        out["connection_groups"] = (
            capo_cloudfront.types.connection_group_summary_list.deserialize_xml(
                child_connection_groups
            )
        )
    return out

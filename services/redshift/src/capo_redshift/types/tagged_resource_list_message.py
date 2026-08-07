"""Generated from Smithy shape ``com.amazonaws.redshift#TaggedResourceListMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tagged_resource_list


class TaggedResourceListMessage(TypedDict, closed=True):
    tagged_resources: NotRequired[
        "capo_redshift.types.tagged_resource_list.TaggedResourceList"
    ]
    """<p>A list of tags with their associated resources.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TaggedResourceListMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tagged_resources" in value:
        import capo_redshift.types.tagged_resource_list

        capo_redshift.types.tagged_resource_list.serialize_query(
            value["tagged_resources"], pairs, f"{key_prefix}TaggedResources"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> TaggedResourceListMessage:
    out: TaggedResourceListMessage = {}  # type: ignore[typeddict-item]
    child_tagged_resources = el.find("TaggedResources")
    if child_tagged_resources is not None:
        import capo_redshift.types.tagged_resource_list

        out["tagged_resources"] = (
            capo_redshift.types.tagged_resource_list.deserialize_query(
                child_tagged_resources
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.autoscaling#TagsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.tag_description_list
    import capo_auto_scaling.types.xml_string


class TagsType(TypedDict, closed=True):
    tags: NotRequired["capo_auto_scaling.types.tag_description_list.TagDescriptionList"]
    """<p>One or more tags.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: TagsType, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tags" in value:
        import capo_auto_scaling.types.tag_description_list

        capo_auto_scaling.types.tag_description_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> TagsType:
    out: TagsType = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_auto_scaling.types.tag_description_list

        out["tags"] = capo_auto_scaling.types.tag_description_list.deserialize_query(
            child_tags
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

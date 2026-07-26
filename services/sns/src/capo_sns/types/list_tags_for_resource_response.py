"""Generated from Smithy shape ``com.amazonaws.sns#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_sns.types.tag_list.TagList"]
    """<p>The tags associated with the specified topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tags" in value:
        import capo_sns.types.tag_list

        capo_sns.types.tag_list.serialize_query(value["tags"], pairs, f"{prefix}.Tags")


def deserialize_query(el: Element) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_sns.types.tag_list

        out["tags"] = capo_sns.types.tag_list.deserialize_query(child_tags)
    return out

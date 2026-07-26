"""Generated from Smithy shape ``com.amazonaws.route53profiles#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53profiles.types.tag_map


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "capo_route53profiles.types.tag_map.TagMap"
    """<p> The tags that are associated with the resource that you specified in the <code>ListTagsForResource</code> request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import capo_route53profiles.types.tag_map

    out["Tags"] = capo_route53profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_route53profiles.types.tag_map

        out["tags"] = capo_route53profiles.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out

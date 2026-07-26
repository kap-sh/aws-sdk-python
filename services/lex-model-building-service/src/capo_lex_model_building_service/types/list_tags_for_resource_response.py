"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["capo_lex_model_building_service.types.tag_list.TagList"]
    """<p>The tags associated with a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_lex_model_building_service.types.tag_list

        out["tags"] = capo_lex_model_building_service.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out

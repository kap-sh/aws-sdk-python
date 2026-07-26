"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.tags_model


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags_model: NotRequired["capo_pinpoint.types.tags_model.TagsModel"]


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags_model" in value:
        import capo_pinpoint.types.tags_model

        out["TagsModel"] = capo_pinpoint.types.tags_model.serialize_json(
            value["tags_model"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "TagsModel" in data:
        import capo_pinpoint.types.tags_model

        out["tags_model"] = capo_pinpoint.types.tags_model.deserialize_json(
            data["TagsModel"]
        )
    return out

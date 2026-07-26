"""Generated from Smithy shape ``com.amazonaws.medialive#CreateTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.tags


class CreateTagsRequest(TypedDict, closed=True):
    resource_arn: "capo_medialive.types.__string.__string"
    tags: NotRequired["capo_medialive.types.tags.Tags"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateTagsRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import capo_medialive.types.tags

        out["tags"] = capo_medialive.types.tags.deserialize_json(data["tags"])
    return out

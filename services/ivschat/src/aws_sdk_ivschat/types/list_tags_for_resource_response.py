"""Generated from Smithy shape ``com.amazonaws.ivschat#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "aws_sdk_ivschat.types.tags.Tags"
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivschat.types.tags

    out["tags"] = aws_sdk_ivschat.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_ivschat.types.tags

        out["tags"] = aws_sdk_ivschat.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out

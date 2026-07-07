"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.tag_list


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: "aws_sdk_pinpoint_email.types.tag_list.TagList"
    """<p>An array that lists all the tags that are associated with the resource. Each tag consists of a required tag key (<code>Key</code>) and an associated tag value (<code>Value</code>)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.tag_list

    out["Tags"] = aws_sdk_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_pinpoint_email.types.tag_list

        out["tags"] = aws_sdk_pinpoint_email.types.tag_list.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceResponse.tags required")
    return out

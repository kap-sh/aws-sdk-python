"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.tag_list


class ListTagsForResourceOutput(TypedDict):
    status_code: NotRequired["int"]
    """<p>The status code of the response.</p>"""
    tags: NotRequired["aws_sdk_socialmessaging.types.tag_list.TagList"]
    """<p>The tags for the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "tags" in value:
        import aws_sdk_socialmessaging.types.tag_list

        out["tags"] = aws_sdk_socialmessaging.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "tags" in data:
        import aws_sdk_socialmessaging.types.tag_list

        out["tags"] = aws_sdk_socialmessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out

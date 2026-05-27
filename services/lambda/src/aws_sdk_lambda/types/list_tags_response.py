"""Generated from Smithy shape ``com.amazonaws.lambda#ListTagsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.tags


class ListTagsResponse(TypedDict):
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    """<p>The function's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsResponse:
    out: ListTagsResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    return out

"""Generated from Smithy shape ``com.amazonaws.personalize#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.tags


class ListTagsForResourceResponse(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_personalize.types.tags.Tags"]
    """<p>The resource's tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_personalize.types.tags

        out["tags"] = aws_sdk_personalize.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out

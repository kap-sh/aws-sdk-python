"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.tags


class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_s3tables.types.tags.Tags"]
    r"""<p>The user-defined tags that are applied to the resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_s3tables.types.tags

        out["tags"] = aws_sdk_s3tables.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_s3tables.types.tags

        out["tags"] = aws_sdk_s3tables.types.tags.deserialize_json(data["tags"])
    return out

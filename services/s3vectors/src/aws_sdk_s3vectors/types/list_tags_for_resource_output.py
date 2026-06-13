"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.tags_map


class ListTagsForResourceOutput(TypedDict):
    tags: "aws_sdk_s3vectors.types.tags_map.TagsMap"
    """<p>The user-defined tags that are applied to the S3 Vectors resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_s3vectors.types.tags_map

    out["tags"] = aws_sdk_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_s3vectors.types.tags_map

        out["tags"] = aws_sdk_s3vectors.types.tags_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    return out

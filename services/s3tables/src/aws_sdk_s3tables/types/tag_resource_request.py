"""Generated from Smithy shape ``com.amazonaws.s3tables#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.resource_arn
    import aws_sdk_s3tables.types.tags


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_s3tables.types.resource_arn.ResourceArn"
    r"""<p>The Amazon Resource Name (ARN) of the Amazon S3 Tables resource that you're applying tags to. The tagged resource can be a table bucket or a table. For a list of all S3 resources that support tagging, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html#manage-tags\">Managing tags for Amazon S3 resources</a>.</p>"""
    tags: "aws_sdk_s3tables.types.tags.Tags"
    r"""<p>The user-defined tag that you want to add to the specified S3 Tables resource. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.tags

    out["tags"] = aws_sdk_s3tables.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_s3tables.types.tags

        out["tags"] = aws_sdk_s3tables.types.tags.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out

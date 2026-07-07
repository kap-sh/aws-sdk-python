"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImagesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_status_filter
    import aws_sdk_ecr.types.tag_status


class DescribeImagesFilter(TypedDict, closed=True):
    tag_status: NotRequired["aws_sdk_ecr.types.tag_status.TagStatus"]
    """<p>The tag status with which to filter your <a>DescribeImages</a> results. You can filter results based on whether they are <code>TAGGED</code> or <code>UNTAGGED</code>.</p>"""
    image_status: NotRequired["aws_sdk_ecr.types.image_status_filter.ImageStatusFilter"]
    """<p>The image status with which to filter your <a>DescribeImages</a> results. Valid values are <code>ACTIVE</code>, <code>ARCHIVED</code>, and <code>ACTIVATING</code>. If not specified, only images with <code>ACTIVE</code> status are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImagesFilter) -> dict:
    out: dict = {}
    if "tag_status" in value:
        import aws_sdk_ecr.types.tag_status

        out["tagStatus"] = aws_sdk_ecr.types.tag_status.serialize_aws_json_1_1(
            value["tag_status"]
        )
    if "image_status" in value:
        import aws_sdk_ecr.types.image_status_filter

        out["imageStatus"] = (
            aws_sdk_ecr.types.image_status_filter.serialize_aws_json_1_1(
                value["image_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImagesFilter:
    out: DescribeImagesFilter = {}  # type: ignore[typeddict-item]
    if "tagStatus" in data:
        import aws_sdk_ecr.types.tag_status

        out["tag_status"] = aws_sdk_ecr.types.tag_status.deserialize_aws_json_1_1(
            data["tagStatus"]
        )
    if "imageStatus" in data:
        import aws_sdk_ecr.types.image_status_filter

        out["image_status"] = (
            aws_sdk_ecr.types.image_status_filter.deserialize_aws_json_1_1(
                data["imageStatus"]
            )
        )
    return out

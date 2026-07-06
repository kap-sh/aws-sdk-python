"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.tag_status


class LifecyclePolicyPreviewFilter(TypedDict, closed=True):
    tag_status: NotRequired["aws_sdk_ecr.types.tag_status.TagStatus"]
    """<p>The tag status of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewFilter) -> dict:
    out: dict = {}
    if "tag_status" in value:
        import aws_sdk_ecr.types.tag_status

        out["tagStatus"] = aws_sdk_ecr.types.tag_status.serialize_aws_json_1_1(
            value["tag_status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyPreviewFilter:
    out: LifecyclePolicyPreviewFilter = {}  # type: ignore[typeddict-item]
    if "tagStatus" in data:
        import aws_sdk_ecr.types.tag_status

        out["tag_status"] = aws_sdk_ecr.types.tag_status.deserialize_aws_json_1_1(
            data["tagStatus"]
        )
    return out

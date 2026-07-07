"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_count
    import aws_sdk_ecr.types.transitioning_image_total_counts


class LifecyclePolicyPreviewSummary(TypedDict, closed=True):
    expiring_image_total_count: NotRequired["aws_sdk_ecr.types.image_count.ImageCount"]
    """<p>The number of expiring images.</p>"""
    transitioning_image_total_counts: NotRequired[
        "aws_sdk_ecr.types.transitioning_image_total_counts.TransitioningImageTotalCounts"
    ]
    """<p>The total count of images that will be transitioned to each storage class. This field is only present if at least one image will be transitoned in the summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewSummary) -> dict:
    out: dict = {}
    if "expiring_image_total_count" in value:
        out["expiringImageTotalCount"] = value["expiring_image_total_count"]
    if "transitioning_image_total_counts" in value:
        import aws_sdk_ecr.types.transitioning_image_total_counts

        out["transitioningImageTotalCounts"] = (
            aws_sdk_ecr.types.transitioning_image_total_counts.serialize_aws_json_1_1(
                value["transitioning_image_total_counts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyPreviewSummary:
    out: LifecyclePolicyPreviewSummary = {}  # type: ignore[typeddict-item]
    if "expiringImageTotalCount" in data:
        out["expiring_image_total_count"] = data["expiringImageTotalCount"]
    if "transitioningImageTotalCounts" in data:
        import aws_sdk_ecr.types.transitioning_image_total_counts

        out["transitioning_image_total_counts"] = (
            aws_sdk_ecr.types.transitioning_image_total_counts.deserialize_aws_json_1_1(
                data["transitioningImageTotalCounts"]
            )
        )
    return out

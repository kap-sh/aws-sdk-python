"""Generated from Smithy shape ``com.amazonaws.ecr#TransitioningImageTotalCount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_count
    import capo_ecr.types.lifecycle_policy_target_storage_class


class TransitioningImageTotalCount(TypedDict, closed=True):
    target_storage_class: NotRequired[
        "capo_ecr.types.lifecycle_policy_target_storage_class.LifecyclePolicyTargetStorageClass"
    ]
    """<p>The target storage class.</p>"""
    image_total_count: NotRequired["capo_ecr.types.image_count.ImageCount"]
    """<p>The total number of images transitioning to the storage class.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransitioningImageTotalCount) -> dict:
    out: dict = {}
    if "target_storage_class" in value:
        import capo_ecr.types.lifecycle_policy_target_storage_class

        out["targetStorageClass"] = (
            capo_ecr.types.lifecycle_policy_target_storage_class.serialize_aws_json_1_1(
                value["target_storage_class"]
            )
        )
    if "image_total_count" in value:
        out["imageTotalCount"] = value["image_total_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransitioningImageTotalCount:
    out: TransitioningImageTotalCount = {}  # type: ignore[typeddict-item]
    if "targetStorageClass" in data:
        import capo_ecr.types.lifecycle_policy_target_storage_class

        out["target_storage_class"] = (
            capo_ecr.types.lifecycle_policy_target_storage_class.deserialize_aws_json_1_1(
                data["targetStorageClass"]
            )
        )
    if "imageTotalCount" in data:
        out["image_total_count"] = data["imageTotalCount"]
    return out

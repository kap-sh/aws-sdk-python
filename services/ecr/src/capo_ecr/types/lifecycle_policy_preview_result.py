"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyPreviewResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_digest
    import capo_ecr.types.image_tag_list
    import capo_ecr.types.lifecycle_policy_rule_action
    import capo_ecr.types.lifecycle_policy_rule_priority
    import capo_ecr.types.lifecycle_policy_storage_class
    import capo_ecr.types.push_timestamp


class LifecyclePolicyPreviewResult(TypedDict, closed=True):
    image_tags: NotRequired["capo_ecr.types.image_tag_list.ImageTagList"]
    """<p>The list of tags associated with this image.</p>"""
    image_digest: NotRequired["capo_ecr.types.image_digest.ImageDigest"]
    """<p>The <code>sha256</code> digest of the image manifest.</p>"""
    image_pushed_at: NotRequired["capo_ecr.types.push_timestamp.PushTimestamp"]
    """<p>The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository.</p>"""
    action: NotRequired[
        "capo_ecr.types.lifecycle_policy_rule_action.LifecyclePolicyRuleAction"
    ]
    """<p>The type of action to be taken.</p>"""
    applied_rule_priority: NotRequired[
        "capo_ecr.types.lifecycle_policy_rule_priority.LifecyclePolicyRulePriority"
    ]
    """<p>The priority of the applied rule.</p>"""
    storage_class: NotRequired[
        "capo_ecr.types.lifecycle_policy_storage_class.LifecyclePolicyStorageClass"
    ]
    """<p>The storage class of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyPreviewResult) -> dict:
    out: dict = {}
    if "image_tags" in value:
        import capo_ecr.types.image_tag_list

        out["imageTags"] = capo_ecr.types.image_tag_list.serialize_aws_json_1_1(
            value["image_tags"]
        )
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "image_pushed_at" in value:
        import capo_ecr.types.push_timestamp

        out["imagePushedAt"] = capo_ecr.types.push_timestamp.serialize_aws_json_1_1(
            value["image_pushed_at"]
        )
    if "action" in value:
        import capo_ecr.types.lifecycle_policy_rule_action

        out["action"] = (
            capo_ecr.types.lifecycle_policy_rule_action.serialize_aws_json_1_1(
                value["action"]
            )
        )
    if "applied_rule_priority" in value:
        out["appliedRulePriority"] = value["applied_rule_priority"]
    if "storage_class" in value:
        import capo_ecr.types.lifecycle_policy_storage_class

        out["storageClass"] = (
            capo_ecr.types.lifecycle_policy_storage_class.serialize_aws_json_1_1(
                value["storage_class"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyPreviewResult:
    out: LifecyclePolicyPreviewResult = {}  # type: ignore[typeddict-item]
    if "imageTags" in data:
        import capo_ecr.types.image_tag_list

        out["image_tags"] = capo_ecr.types.image_tag_list.deserialize_aws_json_1_1(
            data["imageTags"]
        )
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "imagePushedAt" in data:
        import capo_ecr.types.push_timestamp

        out["image_pushed_at"] = capo_ecr.types.push_timestamp.deserialize_aws_json_1_1(
            data["imagePushedAt"]
        )
    if "action" in data:
        import capo_ecr.types.lifecycle_policy_rule_action

        out["action"] = (
            capo_ecr.types.lifecycle_policy_rule_action.deserialize_aws_json_1_1(
                data["action"]
            )
        )
    if "appliedRulePriority" in data:
        out["applied_rule_priority"] = data["appliedRulePriority"]
    if "storageClass" in data:
        import capo_ecr.types.lifecycle_policy_storage_class

        out["storage_class"] = (
            capo_ecr.types.lifecycle_policy_storage_class.deserialize_aws_json_1_1(
                data["storageClass"]
            )
        )
    return out

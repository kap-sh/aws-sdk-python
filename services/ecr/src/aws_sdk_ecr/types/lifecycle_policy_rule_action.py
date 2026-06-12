"""Generated from Smithy shape ``com.amazonaws.ecr#LifecyclePolicyRuleAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_action_type
    import aws_sdk_ecr.types.lifecycle_policy_target_storage_class


class LifecyclePolicyRuleAction(TypedDict):
    type: NotRequired["aws_sdk_ecr.types.image_action_type.ImageActionType"]
    """<p>The type of action to be taken.</p>"""
    target_storage_class: NotRequired[
        "aws_sdk_ecr.types.lifecycle_policy_target_storage_class.LifecyclePolicyTargetStorageClass"
    ]
    """<p>The target storage class for the action. This is only present when the <code>type</code> is <code>TRANSITION.</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecyclePolicyRuleAction) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_ecr.types.image_action_type

        out["type"] = aws_sdk_ecr.types.image_action_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "target_storage_class" in value:
        import aws_sdk_ecr.types.lifecycle_policy_target_storage_class

        out["targetStorageClass"] = (
            aws_sdk_ecr.types.lifecycle_policy_target_storage_class.serialize_aws_json_1_1(
                value["target_storage_class"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecyclePolicyRuleAction:
    out: LifecyclePolicyRuleAction = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_ecr.types.image_action_type

        out["type"] = aws_sdk_ecr.types.image_action_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "targetStorageClass" in data:
        import aws_sdk_ecr.types.lifecycle_policy_target_storage_class

        out["target_storage_class"] = (
            aws_sdk_ecr.types.lifecycle_policy_target_storage_class.deserialize_aws_json_1_1(
                data["targetStorageClass"]
            )
        )
    return out

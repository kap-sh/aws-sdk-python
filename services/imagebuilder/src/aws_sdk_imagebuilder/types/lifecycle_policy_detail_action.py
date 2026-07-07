"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type


class LifecyclePolicyDetailAction(TypedDict, closed=True):
    type: "aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type.LifecyclePolicyDetailActionType"
    """<p>Specifies the lifecycle action to take.</p>"""
    include_resources: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources.LifecyclePolicyDetailActionIncludeResources"
    ]
    """<p>Specifies the resources that the lifecycle policy applies to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailAction) -> dict:
    out: dict = {}
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type

    out["type"] = (
        aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type.serialize_json(
            value["type"]
        )
    )
    if "include_resources" in value:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources

        out["includeResources"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources.serialize_json(
                value["include_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailAction:
    out: LifecyclePolicyDetailAction = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type

        out["type"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("LifecyclePolicyDetailAction.type required")
    if "includeResources" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources

        out["include_resources"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_detail_action_include_resources.deserialize_json(
                data["includeResources"]
            )
        )
    return out

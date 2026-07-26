"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution_resource_action_name
    import capo_imagebuilder.types.non_empty_string


class LifecycleExecutionResourceAction(TypedDict, closed=True):
    name: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_resource_action_name.LifecycleExecutionResourceActionName"
    ]
    """<p>The name of the resource that was identified for a lifecycle policy action.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason why the lifecycle policy action is taken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourceAction) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_imagebuilder.types.lifecycle_execution_resource_action_name

        out["name"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_action_name.serialize_json(
                value["name"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> LifecycleExecutionResourceAction:
    out: LifecycleExecutionResourceAction = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_imagebuilder.types.lifecycle_execution_resource_action_name

        out["name"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_action_name.deserialize_json(
                data["name"]
            )
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out

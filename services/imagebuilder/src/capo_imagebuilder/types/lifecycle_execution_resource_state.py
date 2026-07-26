"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution_resource_status
    import capo_imagebuilder.types.non_empty_string


class LifecycleExecutionResourceState(TypedDict, closed=True):
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_resource_status.LifecycleExecutionResourceStatus"
    ]
    """<p>The runtime status of the lifecycle action taken for the impacted resource.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Messaging that clarifies the reason for the assigned status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourceState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_imagebuilder.types.lifecycle_execution_resource_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_status.serialize_json(
                value["status"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> LifecycleExecutionResourceState:
    out: LifecycleExecutionResourceState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_imagebuilder.types.lifecycle_execution_resource_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_execution_resource_status.deserialize_json(
                data["status"]
            )
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out

"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution_status
    import capo_imagebuilder.types.non_empty_string


class LifecycleExecutionState(TypedDict, closed=True):
    status: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_status.LifecycleExecutionStatus"
    ]
    """<p>The runtime status of the lifecycle execution.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionState) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_imagebuilder.types.lifecycle_execution_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_execution_status.serialize_json(
                value["status"]
            )
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> LifecycleExecutionState:
    out: LifecycleExecutionState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_imagebuilder.types.lifecycle_execution_status

        out["status"] = (
            capo_imagebuilder.types.lifecycle_execution_status.deserialize_json(
                data["status"]
            )
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out

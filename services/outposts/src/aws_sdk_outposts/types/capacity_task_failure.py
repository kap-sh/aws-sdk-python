"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.capacity_task_failure_type
    import aws_sdk_outposts.types.capacity_task_status_reason


class CapacityTaskFailure(TypedDict, closed=True):
    reason: (
        "aws_sdk_outposts.types.capacity_task_status_reason.CapacityTaskStatusReason"
    )
    """<p>The reason that the specified capacity task failed.</p>"""
    type: NotRequired[
        "aws_sdk_outposts.types.capacity_task_failure_type.CapacityTaskFailureType"
    ]
    """<p>The type of failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskFailure) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    if "type" in value:
        import aws_sdk_outposts.types.capacity_task_failure_type

        out["Type"] = aws_sdk_outposts.types.capacity_task_failure_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> CapacityTaskFailure:
    out: CapacityTaskFailure = {}  # type: ignore[typeddict-item]
    if "Reason" in data:
        out["reason"] = data["Reason"]
    else:
        raise DeserializationError("CapacityTaskFailure.reason required")
    if "Type" in data:
        import aws_sdk_outposts.types.capacity_task_failure_type

        out["type"] = (
            aws_sdk_outposts.types.capacity_task_failure_type.deserialize_json(
                data["Type"]
            )
        )
    return out

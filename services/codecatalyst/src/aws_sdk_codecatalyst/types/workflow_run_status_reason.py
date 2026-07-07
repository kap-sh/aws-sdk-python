"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowRunStatusReason``."""

from typing_extensions import TypedDict


class WorkflowRunStatusReason(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunStatusReason) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> WorkflowRunStatusReason:
    out: WorkflowRunStatusReason = {}  # type: ignore[typeddict-item]
    return out

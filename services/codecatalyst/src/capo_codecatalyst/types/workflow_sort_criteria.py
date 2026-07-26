"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowSortCriteria``."""

from typing_extensions import TypedDict


class WorkflowSortCriteria(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowSortCriteria) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> WorkflowSortCriteria:
    out: WorkflowSortCriteria = {}  # type: ignore[typeddict-item]
    return out

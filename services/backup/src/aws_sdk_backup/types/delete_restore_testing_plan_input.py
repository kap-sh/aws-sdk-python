"""Generated from Smithy shape ``com.amazonaws.backup#DeleteRestoreTestingPlanInput``."""

from typing import TypedDict


class DeleteRestoreTestingPlanInput(TypedDict):
    restore_testing_plan_name: "str"
    """<p>Required unique name of the restore testing plan you wish to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRestoreTestingPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRestoreTestingPlanInput:
    out: DeleteRestoreTestingPlanInput = {}  # type: ignore[typeddict-item]
    return out

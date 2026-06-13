"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingPlanInput``."""

from typing import TypedDict


class GetRestoreTestingPlanInput(TypedDict):
    restore_testing_plan_name: "str"
    """<p>Required unique name of the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingPlanInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRestoreTestingPlanInput:
    out: GetRestoreTestingPlanInput = {}  # type: ignore[typeddict-item]
    return out

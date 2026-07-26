"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingSelectionInput``."""

from typing_extensions import TypedDict


class GetRestoreTestingSelectionInput(TypedDict, closed=True):
    restore_testing_plan_name: "str"
    """<p>Required unique name of the restore testing plan.</p>"""
    restore_testing_selection_name: "str"
    """<p>Required unique name of the restore testing selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingSelectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRestoreTestingSelectionInput:
    out: GetRestoreTestingSelectionInput = {}  # type: ignore[typeddict-item]
    return out

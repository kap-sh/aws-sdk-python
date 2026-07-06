"""Generated from Smithy shape ``com.amazonaws.backup#DeleteRestoreTestingSelectionInput``."""

from typing_extensions import TypedDict


class DeleteRestoreTestingSelectionInput(TypedDict, closed=True):
    restore_testing_plan_name: "str"
    """<p>Required unique name of the restore testing plan that contains the restore testing selection you wish to delete.</p>"""
    restore_testing_selection_name: "str"
    """<p>Required unique name of the restore testing selection you wish to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRestoreTestingSelectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRestoreTestingSelectionInput:
    out: DeleteRestoreTestingSelectionInput = {}  # type: ignore[typeddict-item]
    return out

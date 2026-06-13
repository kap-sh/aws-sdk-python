"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingSelectionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_testing_selection_for_get


class GetRestoreTestingSelectionOutput(TypedDict):
    restore_testing_selection: "aws_sdk_backup.types.restore_testing_selection_for_get.RestoreTestingSelectionForGet"
    """<p>Unique name of the restore testing selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingSelectionOutput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.restore_testing_selection_for_get

    out["RestoreTestingSelection"] = (
        aws_sdk_backup.types.restore_testing_selection_for_get.serialize_json(
            value["restore_testing_selection"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRestoreTestingSelectionOutput:
    out: GetRestoreTestingSelectionOutput = {}  # type: ignore[typeddict-item]
    if "RestoreTestingSelection" in data:
        import aws_sdk_backup.types.restore_testing_selection_for_get

        out["restore_testing_selection"] = (
            aws_sdk_backup.types.restore_testing_selection_for_get.deserialize_json(
                data["RestoreTestingSelection"]
            )
        )
    else:
        raise DeserializationError(
            "GetRestoreTestingSelectionOutput.restore_testing_selection required"
        )
    return out

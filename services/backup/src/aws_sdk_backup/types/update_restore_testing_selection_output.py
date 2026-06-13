"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingSelectionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class UpdateRestoreTestingSelectionOutput(TypedDict):
    creation_time: "datetime.datetime"
    """<p>The time the resource testing selection was updated successfully.</p>"""
    restore_testing_plan_arn: "str"
    """<p>Unique string that is the name of the restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The restore testing plan with which the updated restore testing selection is associated.</p>"""
    restore_testing_selection_name: "str"
    """<p>The returned restore testing selection name.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the update completed for the restore testing selection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingSelectionOutput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types._prelude.timestamp

    out["CreationTime"] = aws_sdk_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    out["RestoreTestingSelectionName"] = value["restore_testing_selection_name"]
    import aws_sdk_backup.types._prelude.timestamp

    out["UpdateTime"] = aws_sdk_backup.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingSelectionOutput:
    out: UpdateRestoreTestingSelectionOutput = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import aws_sdk_backup.types._prelude.timestamp

        out["creation_time"] = aws_sdk_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionOutput.creation_time required"
        )
    if "RestoreTestingPlanArn" in data:
        out["restore_testing_plan_arn"] = data["RestoreTestingPlanArn"]
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionOutput.restore_testing_plan_arn required"
        )
    if "RestoreTestingPlanName" in data:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionOutput.restore_testing_plan_name required"
        )
    if "RestoreTestingSelectionName" in data:
        out["restore_testing_selection_name"] = data["RestoreTestingSelectionName"]
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionOutput.restore_testing_selection_name required"
        )
    if "UpdateTime" in data:
        import aws_sdk_backup.types._prelude.timestamp

        out["update_time"] = aws_sdk_backup.types._prelude.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingSelectionOutput.update_time required"
        )
    return out

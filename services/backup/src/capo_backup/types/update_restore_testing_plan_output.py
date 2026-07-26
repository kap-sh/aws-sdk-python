"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class UpdateRestoreTestingPlanOutput(TypedDict, closed=True):
    creation_time: "datetime.datetime"
    """<p>The time the resource testing plan was created.</p>"""
    restore_testing_plan_arn: "str"
    """<p>Unique ARN (Amazon Resource Name) of the restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the update completed for the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingPlanOutput) -> dict:
    out: dict = {}
    import capo_backup.types._prelude.timestamp

    out["CreationTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    out["RestoreTestingPlanName"] = value["restore_testing_plan_name"]
    import capo_backup.types._prelude.timestamp

    out["UpdateTime"] = capo_backup.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingPlanOutput:
    out: UpdateRestoreTestingPlanOutput = {}  # type: ignore[typeddict-item]
    if "CreationTime" in data:
        import capo_backup.types._prelude.timestamp

        out["creation_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingPlanOutput.creation_time required"
        )
    if "RestoreTestingPlanArn" in data:
        out["restore_testing_plan_arn"] = data["RestoreTestingPlanArn"]
    else:
        raise DeserializationError(
            "UpdateRestoreTestingPlanOutput.restore_testing_plan_arn required"
        )
    if "RestoreTestingPlanName" in data:
        out["restore_testing_plan_name"] = data["RestoreTestingPlanName"]
    else:
        raise DeserializationError(
            "UpdateRestoreTestingPlanOutput.restore_testing_plan_name required"
        )
    if "UpdateTime" in data:
        import capo_backup.types._prelude.timestamp

        out["update_time"] = capo_backup.types._prelude.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingPlanOutput.update_time required"
        )
    return out

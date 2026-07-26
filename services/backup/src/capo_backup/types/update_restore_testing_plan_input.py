"""Generated from Smithy shape ``com.amazonaws.backup#UpdateRestoreTestingPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_plan_for_update


class UpdateRestoreTestingPlanInput(TypedDict, closed=True):
    restore_testing_plan: (
        "capo_backup.types.restore_testing_plan_for_update.RestoreTestingPlanForUpdate"
    )
    """<p>Specifies the body of a restore testing plan.</p>"""
    restore_testing_plan_name: "str"
    """<p>The name of the restore testing plan name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRestoreTestingPlanInput) -> dict:
    out: dict = {}
    import capo_backup.types.restore_testing_plan_for_update

    out["RestoreTestingPlan"] = (
        capo_backup.types.restore_testing_plan_for_update.serialize_json(
            value["restore_testing_plan"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateRestoreTestingPlanInput:
    out: UpdateRestoreTestingPlanInput = {}  # type: ignore[typeddict-item]
    if "RestoreTestingPlan" in data:
        import capo_backup.types.restore_testing_plan_for_update

        out["restore_testing_plan"] = (
            capo_backup.types.restore_testing_plan_for_update.deserialize_json(
                data["RestoreTestingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRestoreTestingPlanInput.restore_testing_plan required"
        )
    return out

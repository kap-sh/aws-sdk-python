"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.restore_testing_plan_for_get


class GetRestoreTestingPlanOutput(TypedDict, closed=True):
    restore_testing_plan: (
        "aws_sdk_backup.types.restore_testing_plan_for_get.RestoreTestingPlanForGet"
    )
    """<p>Specifies the body of a restore testing plan. Includes <code>RestoreTestingPlanName</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingPlanOutput) -> dict:
    out: dict = {}
    import aws_sdk_backup.types.restore_testing_plan_for_get

    out["RestoreTestingPlan"] = (
        aws_sdk_backup.types.restore_testing_plan_for_get.serialize_json(
            value["restore_testing_plan"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetRestoreTestingPlanOutput:
    out: GetRestoreTestingPlanOutput = {}  # type: ignore[typeddict-item]
    if "RestoreTestingPlan" in data:
        import aws_sdk_backup.types.restore_testing_plan_for_get

        out["restore_testing_plan"] = (
            aws_sdk_backup.types.restore_testing_plan_for_get.deserialize_json(
                data["RestoreTestingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "GetRestoreTestingPlanOutput.restore_testing_plan required"
        )
    return out

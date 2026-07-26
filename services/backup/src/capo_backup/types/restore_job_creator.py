"""Generated from Smithy shape ``com.amazonaws.backup#RestoreJobCreator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn


class RestoreJobCreator(TypedDict, closed=True):
    restore_testing_plan_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreJobCreator) -> dict:
    out: dict = {}
    if "restore_testing_plan_arn" in value:
        out["RestoreTestingPlanArn"] = value["restore_testing_plan_arn"]
    return out


def deserialize_json(data: dict) -> RestoreJobCreator:
    out: RestoreJobCreator = {}  # type: ignore[typeddict-item]
    if "RestoreTestingPlanArn" in data:
        out["restore_testing_plan_arn"] = data["RestoreTestingPlanArn"]
    return out

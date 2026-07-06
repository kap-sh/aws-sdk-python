"""Generated from Smithy shape ``com.amazonaws.medialive#BatchUpdateScheduleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.batch_schedule_action_create_result
    import aws_sdk_medialive.types.batch_schedule_action_delete_result


class BatchUpdateScheduleResponse(TypedDict, closed=True):
    creates: NotRequired[
        "aws_sdk_medialive.types.batch_schedule_action_create_result.BatchScheduleActionCreateResult"
    ]
    """Schedule actions created in the schedule."""
    deletes: NotRequired[
        "aws_sdk_medialive.types.batch_schedule_action_delete_result.BatchScheduleActionDeleteResult"
    ]
    """Schedule actions deleted from the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateScheduleResponse) -> dict:
    out: dict = {}
    if "creates" in value:
        import aws_sdk_medialive.types.batch_schedule_action_create_result

        out["creates"] = (
            aws_sdk_medialive.types.batch_schedule_action_create_result.serialize_json(
                value["creates"]
            )
        )
    if "deletes" in value:
        import aws_sdk_medialive.types.batch_schedule_action_delete_result

        out["deletes"] = (
            aws_sdk_medialive.types.batch_schedule_action_delete_result.serialize_json(
                value["deletes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateScheduleResponse:
    out: BatchUpdateScheduleResponse = {}  # type: ignore[typeddict-item]
    if "creates" in data:
        import aws_sdk_medialive.types.batch_schedule_action_create_result

        out["creates"] = (
            aws_sdk_medialive.types.batch_schedule_action_create_result.deserialize_json(
                data["creates"]
            )
        )
    if "deletes" in data:
        import aws_sdk_medialive.types.batch_schedule_action_delete_result

        out["deletes"] = (
            aws_sdk_medialive.types.batch_schedule_action_delete_result.deserialize_json(
                data["deletes"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.medialive#BatchUpdateScheduleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.batch_schedule_action_create_request
    import aws_sdk_medialive.types.batch_schedule_action_delete_request


class BatchUpdateScheduleRequest(TypedDict):
    channel_id: "aws_sdk_medialive.types.__string.__string"
    """Id of the channel whose schedule is being updated."""
    creates: NotRequired[
        "aws_sdk_medialive.types.batch_schedule_action_create_request.BatchScheduleActionCreateRequest"
    ]
    """Schedule actions to create in the schedule."""
    deletes: NotRequired[
        "aws_sdk_medialive.types.batch_schedule_action_delete_request.BatchScheduleActionDeleteRequest"
    ]
    """Schedule actions to delete from the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateScheduleRequest) -> dict:
    out: dict = {}
    if "creates" in value:
        import aws_sdk_medialive.types.batch_schedule_action_create_request

        out["creates"] = (
            aws_sdk_medialive.types.batch_schedule_action_create_request.serialize_json(
                value["creates"]
            )
        )
    if "deletes" in value:
        import aws_sdk_medialive.types.batch_schedule_action_delete_request

        out["deletes"] = (
            aws_sdk_medialive.types.batch_schedule_action_delete_request.serialize_json(
                value["deletes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateScheduleRequest:
    out: BatchUpdateScheduleRequest = {}  # type: ignore[typeddict-item]
    if "creates" in data:
        import aws_sdk_medialive.types.batch_schedule_action_create_request

        out["creates"] = (
            aws_sdk_medialive.types.batch_schedule_action_create_request.deserialize_json(
                data["creates"]
            )
        )
    if "deletes" in data:
        import aws_sdk_medialive.types.batch_schedule_action_delete_request

        out["deletes"] = (
            aws_sdk_medialive.types.batch_schedule_action_delete_request.deserialize_json(
                data["deletes"]
            )
        )
    return out

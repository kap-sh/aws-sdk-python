"""Generated from Smithy shape ``com.amazonaws.medialive#BatchUpdateScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.batch_schedule_action_create_request
    import capo_medialive.types.batch_schedule_action_delete_request


class BatchUpdateScheduleRequest(TypedDict, closed=True):
    channel_id: "capo_medialive.types.__string.__string"
    """Id of the channel whose schedule is being updated."""
    creates: NotRequired[
        "capo_medialive.types.batch_schedule_action_create_request.BatchScheduleActionCreateRequest"
    ]
    """Schedule actions to create in the schedule."""
    deletes: NotRequired[
        "capo_medialive.types.batch_schedule_action_delete_request.BatchScheduleActionDeleteRequest"
    ]
    """Schedule actions to delete from the schedule."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateScheduleRequest) -> dict:
    out: dict = {}
    if "creates" in value:
        import capo_medialive.types.batch_schedule_action_create_request

        out["creates"] = (
            capo_medialive.types.batch_schedule_action_create_request.serialize_json(
                value["creates"]
            )
        )
    if "deletes" in value:
        import capo_medialive.types.batch_schedule_action_delete_request

        out["deletes"] = (
            capo_medialive.types.batch_schedule_action_delete_request.serialize_json(
                value["deletes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateScheduleRequest:
    out: BatchUpdateScheduleRequest = {}  # type: ignore[typeddict-item]
    if "creates" in data:
        import capo_medialive.types.batch_schedule_action_create_request

        out["creates"] = (
            capo_medialive.types.batch_schedule_action_create_request.deserialize_json(
                data["creates"]
            )
        )
    if "deletes" in data:
        import capo_medialive.types.batch_schedule_action_delete_request

        out["deletes"] = (
            capo_medialive.types.batch_schedule_action_delete_request.deserialize_json(
                data["deletes"]
            )
        )
    return out

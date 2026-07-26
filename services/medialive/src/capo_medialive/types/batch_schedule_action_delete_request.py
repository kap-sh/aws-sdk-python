"""Generated from Smithy shape ``com.amazonaws.medialive#BatchScheduleActionDeleteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string


class BatchScheduleActionDeleteRequest(TypedDict, closed=True):
    action_names: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """A list of schedule actions to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: BatchScheduleActionDeleteRequest) -> dict:
    out: dict = {}
    if "action_names" in value:
        import capo_medialive.types.__list_of__string

        out["actionNames"] = capo_medialive.types.__list_of__string.serialize_json(
            value["action_names"]
        )
    return out


def deserialize_json(data: dict) -> BatchScheduleActionDeleteRequest:
    out: BatchScheduleActionDeleteRequest = {}  # type: ignore[typeddict-item]
    if "actionNames" in data:
        import capo_medialive.types.__list_of__string

        out["action_names"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["actionNames"]
        )
    return out

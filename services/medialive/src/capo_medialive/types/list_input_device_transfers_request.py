"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputDeviceTransfersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.max_results


class ListInputDeviceTransfersRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["capo_medialive.types.__string.__string"]
    transfer_type: NotRequired["capo_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputDeviceTransfersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputDeviceTransfersRequest:
    out: ListInputDeviceTransfersRequest = {}  # type: ignore[typeddict-item]
    return out

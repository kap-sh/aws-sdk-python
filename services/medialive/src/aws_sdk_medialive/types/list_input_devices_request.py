"""Generated from Smithy shape ``com.amazonaws.medialive#ListInputDevicesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.max_results


class ListInputDevicesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_medialive.types.max_results.MaxResults"]
    next_token: NotRequired["aws_sdk_medialive.types.__string.__string"]


# --- restJson1 ser/de ---
def serialize_json(value: ListInputDevicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInputDevicesRequest:
    out: ListInputDevicesRequest = {}  # type: ignore[typeddict-item]
    return out

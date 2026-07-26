"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#UpdateDetectorRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.update_detector_request

UpdateDetectorRequests: TypeAlias = list[
    "capo_iot_events_data.types.update_detector_request.UpdateDetectorRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorRequests) -> list:
    import capo_iot_events_data.types.update_detector_request

    out: list = []
    for item in value:
        out.append(
            capo_iot_events_data.types.update_detector_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpdateDetectorRequests:
    import capo_iot_events_data.types.update_detector_request

    out: UpdateDetectorRequests = []
    for item in data:
        out.append(
            capo_iot_events_data.types.update_detector_request.deserialize_json(item)
        )
    return out

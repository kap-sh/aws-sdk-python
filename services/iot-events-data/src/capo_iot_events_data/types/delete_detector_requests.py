"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DeleteDetectorRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.delete_detector_request

DeleteDetectorRequests: TypeAlias = list[
    "capo_iot_events_data.types.delete_detector_request.DeleteDetectorRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDetectorRequests) -> list:
    import capo_iot_events_data.types.delete_detector_request

    out: list = []
    for item in value:
        out.append(
            capo_iot_events_data.types.delete_detector_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteDetectorRequests:
    import capo_iot_events_data.types.delete_detector_request

    out: DeleteDetectorRequests = []
    for item in data:
        out.append(
            capo_iot_events_data.types.delete_detector_request.deserialize_json(item)
        )
    return out

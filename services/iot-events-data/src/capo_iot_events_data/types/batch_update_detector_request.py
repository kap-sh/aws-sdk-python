"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchUpdateDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events_data.types.update_detector_requests


class BatchUpdateDetectorRequest(TypedDict, closed=True):
    detectors: (
        "capo_iot_events_data.types.update_detector_requests.UpdateDetectorRequests"
    )
    """<p>The list of detectors (instances) to update, along with the values to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDetectorRequest) -> dict:
    out: dict = {}
    import capo_iot_events_data.types.update_detector_requests

    out["detectors"] = (
        capo_iot_events_data.types.update_detector_requests.serialize_json(
            value["detectors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateDetectorRequest:
    out: BatchUpdateDetectorRequest = {}  # type: ignore[typeddict-item]
    if "detectors" in data:
        import capo_iot_events_data.types.update_detector_requests

        out["detectors"] = (
            capo_iot_events_data.types.update_detector_requests.deserialize_json(
                data["detectors"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateDetectorRequest.detectors required")
    return out

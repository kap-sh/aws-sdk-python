"""Generated from Smithy shape ``com.amazonaws.iotevents#DeleteDetectorModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model_name


class DeleteDetectorModelRequest(TypedDict, closed=True):
    detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName"
    """<p>The name of the detector model to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDetectorModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDetectorModelRequest:
    out: DeleteDetectorModelRequest = {}  # type: ignore[typeddict-item]
    return out

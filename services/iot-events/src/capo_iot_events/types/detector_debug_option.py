"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorDebugOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model_name
    import capo_iot_events.types.key_value


class DetectorDebugOption(TypedDict, closed=True):
    detector_model_name: "capo_iot_events.types.detector_model_name.DetectorModelName"
    """<p>The name of the detector model.</p>"""
    key_value: NotRequired["capo_iot_events.types.key_value.KeyValue"]
    """<p>The value of the input attribute key used to create the detector (the instance of the detector model).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorDebugOption) -> dict:
    out: dict = {}
    out["detectorModelName"] = value["detector_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    return out


def deserialize_json(data: dict) -> DetectorDebugOption:
    out: DetectorDebugOption = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    else:
        raise DeserializationError("DetectorDebugOption.detector_model_name required")
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    return out

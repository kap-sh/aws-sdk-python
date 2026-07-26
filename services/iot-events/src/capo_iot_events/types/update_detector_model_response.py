"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateDetectorModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.detector_model_configuration


class UpdateDetectorModelResponse(TypedDict, closed=True):
    detector_model_configuration: NotRequired[
        "capo_iot_events.types.detector_model_configuration.DetectorModelConfiguration"
    ]
    """<p>Information about how the detector model is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorModelResponse) -> dict:
    out: dict = {}
    if "detector_model_configuration" in value:
        import capo_iot_events.types.detector_model_configuration

        out["detectorModelConfiguration"] = (
            capo_iot_events.types.detector_model_configuration.serialize_json(
                value["detector_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDetectorModelResponse:
    out: UpdateDetectorModelResponse = {}  # type: ignore[typeddict-item]
    if "detectorModelConfiguration" in data:
        import capo_iot_events.types.detector_model_configuration

        out["detector_model_configuration"] = (
            capo_iot_events.types.detector_model_configuration.deserialize_json(
                data["detectorModelConfiguration"]
            )
        )
    return out

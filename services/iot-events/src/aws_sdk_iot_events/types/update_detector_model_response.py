"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateDetectorModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_configuration


class UpdateDetectorModelResponse(TypedDict):
    detector_model_configuration: NotRequired[
        "aws_sdk_iot_events.types.detector_model_configuration.DetectorModelConfiguration"
    ]
    """<p>Information about how the detector model is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorModelResponse) -> dict:
    out: dict = {}
    if "detector_model_configuration" in value:
        import aws_sdk_iot_events.types.detector_model_configuration

        out["detectorModelConfiguration"] = (
            aws_sdk_iot_events.types.detector_model_configuration.serialize_json(
                value["detector_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDetectorModelResponse:
    out: UpdateDetectorModelResponse = {}  # type: ignore[typeddict-item]
    if "detectorModelConfiguration" in data:
        import aws_sdk_iot_events.types.detector_model_configuration

        out["detector_model_configuration"] = (
            aws_sdk_iot_events.types.detector_model_configuration.deserialize_json(
                data["detectorModelConfiguration"]
            )
        )
    return out

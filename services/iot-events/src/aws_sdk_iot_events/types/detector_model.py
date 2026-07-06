"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_configuration
    import aws_sdk_iot_events.types.detector_model_definition


class DetectorModel(TypedDict, closed=True):
    detector_model_definition: NotRequired[
        "aws_sdk_iot_events.types.detector_model_definition.DetectorModelDefinition"
    ]
    """<p>Information that defines how a detector operates.</p>"""
    detector_model_configuration: NotRequired[
        "aws_sdk_iot_events.types.detector_model_configuration.DetectorModelConfiguration"
    ]
    """<p>Information about how the detector is configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModel) -> dict:
    out: dict = {}
    if "detector_model_definition" in value:
        import aws_sdk_iot_events.types.detector_model_definition

        out["detectorModelDefinition"] = (
            aws_sdk_iot_events.types.detector_model_definition.serialize_json(
                value["detector_model_definition"]
            )
        )
    if "detector_model_configuration" in value:
        import aws_sdk_iot_events.types.detector_model_configuration

        out["detectorModelConfiguration"] = (
            aws_sdk_iot_events.types.detector_model_configuration.serialize_json(
                value["detector_model_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectorModel:
    out: DetectorModel = {}  # type: ignore[typeddict-item]
    if "detectorModelDefinition" in data:
        import aws_sdk_iot_events.types.detector_model_definition

        out["detector_model_definition"] = (
            aws_sdk_iot_events.types.detector_model_definition.deserialize_json(
                data["detectorModelDefinition"]
            )
        )
    if "detectorModelConfiguration" in data:
        import aws_sdk_iot_events.types.detector_model_configuration

        out["detector_model_configuration"] = (
            aws_sdk_iot_events.types.detector_model_configuration.deserialize_json(
                data["detectorModelConfiguration"]
            )
        )
    return out

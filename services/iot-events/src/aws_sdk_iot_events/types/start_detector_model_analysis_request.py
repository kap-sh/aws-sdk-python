"""Generated from Smithy shape ``com.amazonaws.iotevents#StartDetectorModelAnalysisRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.detector_model_definition


class StartDetectorModelAnalysisRequest(TypedDict):
    detector_model_definition: (
        "aws_sdk_iot_events.types.detector_model_definition.DetectorModelDefinition"
    )


# --- restJson1 ser/de ---
def serialize_json(value: StartDetectorModelAnalysisRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.detector_model_definition

    out["detectorModelDefinition"] = (
        aws_sdk_iot_events.types.detector_model_definition.serialize_json(
            value["detector_model_definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartDetectorModelAnalysisRequest:
    out: StartDetectorModelAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "detectorModelDefinition" in data:
        import aws_sdk_iot_events.types.detector_model_definition

        out["detector_model_definition"] = (
            aws_sdk_iot_events.types.detector_model_definition.deserialize_json(
                data["detectorModelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "StartDetectorModelAnalysisRequest.detector_model_definition required"
        )
    return out

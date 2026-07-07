"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateDetectorModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.detector_model_definition
    import aws_sdk_iot_events.types.detector_model_description
    import aws_sdk_iot_events.types.detector_model_name
    import aws_sdk_iot_events.types.evaluation_method


class UpdateDetectorModelRequest(TypedDict, closed=True):
    detector_model_name: (
        "aws_sdk_iot_events.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model that is updated.</p>"""
    detector_model_definition: (
        "aws_sdk_iot_events.types.detector_model_definition.DetectorModelDefinition"
    )
    """<p>Information that defines how a detector operates.</p>"""
    detector_model_description: NotRequired[
        "aws_sdk_iot_events.types.detector_model_description.DetectorModelDescription"
    ]
    """<p>A brief description of the detector model.</p>"""
    role_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>"""
    evaluation_method: NotRequired[
        "aws_sdk_iot_events.types.evaluation_method.EvaluationMethod"
    ]
    """<p>Information about the order in which events are evaluated and how actions are executed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorModelRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.detector_model_definition

    out["detectorModelDefinition"] = (
        aws_sdk_iot_events.types.detector_model_definition.serialize_json(
            value["detector_model_definition"]
        )
    )
    if "detector_model_description" in value:
        out["detectorModelDescription"] = value["detector_model_description"]
    out["roleArn"] = value["role_arn"]
    if "evaluation_method" in value:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluationMethod"] = (
            aws_sdk_iot_events.types.evaluation_method.serialize_json(
                value["evaluation_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDetectorModelRequest:
    out: UpdateDetectorModelRequest = {}  # type: ignore[typeddict-item]
    if "detectorModelDefinition" in data:
        import aws_sdk_iot_events.types.detector_model_definition

        out["detector_model_definition"] = (
            aws_sdk_iot_events.types.detector_model_definition.deserialize_json(
                data["detectorModelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateDetectorModelRequest.detector_model_definition required"
        )
    if "detectorModelDescription" in data:
        out["detector_model_description"] = data["detectorModelDescription"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateDetectorModelRequest.role_arn required")
    if "evaluationMethod" in data:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluation_method"] = (
            aws_sdk_iot_events.types.evaluation_method.deserialize_json(
                data["evaluationMethod"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateDetectorModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.attribute_json_path
    import aws_sdk_iot_events.types.detector_model_definition
    import aws_sdk_iot_events.types.detector_model_description
    import aws_sdk_iot_events.types.detector_model_name
    import aws_sdk_iot_events.types.evaluation_method
    import aws_sdk_iot_events.types.tags


class CreateDetectorModelRequest(TypedDict, closed=True):
    detector_model_name: (
        "aws_sdk_iot_events.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model.</p>"""
    detector_model_definition: (
        "aws_sdk_iot_events.types.detector_model_definition.DetectorModelDefinition"
    )
    """<p>Information that defines how the detectors operate.</p>"""
    detector_model_description: NotRequired[
        "aws_sdk_iot_events.types.detector_model_description.DetectorModelDescription"
    ]
    """<p>A brief description of the detector model.</p>"""
    key: NotRequired["aws_sdk_iot_events.types.attribute_json_path.AttributeJsonPath"]
    """<p>The input attribute key used to identify a device or system to create a detector (an instance of the detector model) and then to route each input received to the appropriate detector (instance). This parameter uses a JSON-path expression in the message payload of each input to specify the attribute-value pair that is used to identify the device associated with the input.</p>"""
    role_arn: "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>"""
    tags: NotRequired["aws_sdk_iot_events.types.tags.Tags"]
    """<p>Metadata that can be used to manage the detector model.</p>"""
    evaluation_method: NotRequired[
        "aws_sdk_iot_events.types.evaluation_method.EvaluationMethod"
    ]
    """<p>Information about the order in which events are evaluated and how actions are executed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDetectorModelRequest) -> dict:
    out: dict = {}
    out["detectorModelName"] = value["detector_model_name"]
    import aws_sdk_iot_events.types.detector_model_definition

    out["detectorModelDefinition"] = (
        aws_sdk_iot_events.types.detector_model_definition.serialize_json(
            value["detector_model_definition"]
        )
    )
    if "detector_model_description" in value:
        out["detectorModelDescription"] = value["detector_model_description"]
    if "key" in value:
        out["key"] = value["key"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_iot_events.types.tags

        out["tags"] = aws_sdk_iot_events.types.tags.serialize_json(value["tags"])
    if "evaluation_method" in value:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluationMethod"] = (
            aws_sdk_iot_events.types.evaluation_method.serialize_json(
                value["evaluation_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDetectorModelRequest:
    out: CreateDetectorModelRequest = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    else:
        raise DeserializationError(
            "CreateDetectorModelRequest.detector_model_name required"
        )
    if "detectorModelDefinition" in data:
        import aws_sdk_iot_events.types.detector_model_definition

        out["detector_model_definition"] = (
            aws_sdk_iot_events.types.detector_model_definition.deserialize_json(
                data["detectorModelDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDetectorModelRequest.detector_model_definition required"
        )
    if "detectorModelDescription" in data:
        out["detector_model_description"] = data["detectorModelDescription"]
    if "key" in data:
        out["key"] = data["key"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateDetectorModelRequest.role_arn required")
    if "tags" in data:
        import aws_sdk_iot_events.types.tags

        out["tags"] = aws_sdk_iot_events.types.tags.deserialize_json(data["tags"])
    if "evaluationMethod" in data:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluation_method"] = (
            aws_sdk_iot_events.types.evaluation_method.deserialize_json(
                data["evaluationMethod"]
            )
        )
    return out

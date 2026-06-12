"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.amazon_resource_name
    import aws_sdk_iot_events.types.attribute_json_path
    import aws_sdk_iot_events.types.detector_model_arn
    import aws_sdk_iot_events.types.detector_model_description
    import aws_sdk_iot_events.types.detector_model_name
    import aws_sdk_iot_events.types.detector_model_version
    import aws_sdk_iot_events.types.detector_model_version_status
    import aws_sdk_iot_events.types.evaluation_method
    import aws_sdk_iot_events.types.timestamp


class DetectorModelConfiguration(TypedDict):
    detector_model_name: NotRequired[
        "aws_sdk_iot_events.types.detector_model_name.DetectorModelName"
    ]
    """<p>The name of the detector model.</p>"""
    detector_model_version: NotRequired[
        "aws_sdk_iot_events.types.detector_model_version.DetectorModelVersion"
    ]
    """<p>The version of the detector model.</p>"""
    detector_model_description: NotRequired[
        "aws_sdk_iot_events.types.detector_model_description.DetectorModelDescription"
    ]
    """<p>A brief description of the detector model.</p>"""
    detector_model_arn: NotRequired[
        "aws_sdk_iot_events.types.detector_model_arn.DetectorModelArn"
    ]
    """<p>The ARN of the detector model.</p>"""
    role_arn: NotRequired[
        "aws_sdk_iot_events.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform its operations.</p>"""
    creation_time: NotRequired["aws_sdk_iot_events.types.timestamp.Timestamp"]
    """<p>The time the detector model was created.</p>"""
    last_update_time: NotRequired["aws_sdk_iot_events.types.timestamp.Timestamp"]
    """<p>The time the detector model was last updated.</p>"""
    status: NotRequired[
        "aws_sdk_iot_events.types.detector_model_version_status.DetectorModelVersionStatus"
    ]
    """<p>The status of the detector model.</p>"""
    key: NotRequired["aws_sdk_iot_events.types.attribute_json_path.AttributeJsonPath"]
    """<p>The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information. </p> <p>This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.</p>"""
    evaluation_method: NotRequired[
        "aws_sdk_iot_events.types.evaluation_method.EvaluationMethod"
    ]
    """<p>Information about the order in which events are evaluated and how actions are executed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelConfiguration) -> dict:
    out: dict = {}
    if "detector_model_name" in value:
        out["detectorModelName"] = value["detector_model_name"]
    if "detector_model_version" in value:
        out["detectorModelVersion"] = value["detector_model_version"]
    if "detector_model_description" in value:
        out["detectorModelDescription"] = value["detector_model_description"]
    if "detector_model_arn" in value:
        out["detectorModelArn"] = value["detector_model_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "creation_time" in value:
        import aws_sdk_iot_events.types.timestamp

        out["creationTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_iot_events.types.timestamp

        out["lastUpdateTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    if "status" in value:
        import aws_sdk_iot_events.types.detector_model_version_status

        out["status"] = (
            aws_sdk_iot_events.types.detector_model_version_status.serialize_json(
                value["status"]
            )
        )
    if "key" in value:
        out["key"] = value["key"]
    if "evaluation_method" in value:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluationMethod"] = (
            aws_sdk_iot_events.types.evaluation_method.serialize_json(
                value["evaluation_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectorModelConfiguration:
    out: DetectorModelConfiguration = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    if "detectorModelVersion" in data:
        out["detector_model_version"] = data["detectorModelVersion"]
    if "detectorModelDescription" in data:
        out["detector_model_description"] = data["detectorModelDescription"]
    if "detectorModelArn" in data:
        out["detector_model_arn"] = data["detectorModelArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "creationTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["creation_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["last_update_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    if "status" in data:
        import aws_sdk_iot_events.types.detector_model_version_status

        out["status"] = (
            aws_sdk_iot_events.types.detector_model_version_status.deserialize_json(
                data["status"]
            )
        )
    if "key" in data:
        out["key"] = data["key"]
    if "evaluationMethod" in data:
        import aws_sdk_iot_events.types.evaluation_method

        out["evaluation_method"] = (
            aws_sdk_iot_events.types.evaluation_method.deserialize_json(
                data["evaluationMethod"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.detector_model_arn
    import capo_iot_events.types.detector_model_name
    import capo_iot_events.types.detector_model_version
    import capo_iot_events.types.detector_model_version_status
    import capo_iot_events.types.evaluation_method
    import capo_iot_events.types.timestamp


class DetectorModelVersionSummary(TypedDict, closed=True):
    detector_model_name: NotRequired[
        "capo_iot_events.types.detector_model_name.DetectorModelName"
    ]
    """<p>The name of the detector model.</p>"""
    detector_model_version: NotRequired[
        "capo_iot_events.types.detector_model_version.DetectorModelVersion"
    ]
    """<p>The ID of the detector model version.</p>"""
    detector_model_arn: NotRequired[
        "capo_iot_events.types.detector_model_arn.DetectorModelArn"
    ]
    """<p>The ARN of the detector model version.</p>"""
    role_arn: NotRequired[
        "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the role that grants the detector model permission to perform its tasks.</p>"""
    creation_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The time the detector model version was created.</p>"""
    last_update_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The last time the detector model version was updated.</p>"""
    status: NotRequired[
        "capo_iot_events.types.detector_model_version_status.DetectorModelVersionStatus"
    ]
    """<p>The status of the detector model version.</p>"""
    evaluation_method: NotRequired[
        "capo_iot_events.types.evaluation_method.EvaluationMethod"
    ]
    """<p>Information about the order in which events are evaluated and how actions are executed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelVersionSummary) -> dict:
    out: dict = {}
    if "detector_model_name" in value:
        out["detectorModelName"] = value["detector_model_name"]
    if "detector_model_version" in value:
        out["detectorModelVersion"] = value["detector_model_version"]
    if "detector_model_arn" in value:
        out["detectorModelArn"] = value["detector_model_arn"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "creation_time" in value:
        import capo_iot_events.types.timestamp

        out["creationTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import capo_iot_events.types.timestamp

        out["lastUpdateTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    if "status" in value:
        import capo_iot_events.types.detector_model_version_status

        out["status"] = (
            capo_iot_events.types.detector_model_version_status.serialize_json(
                value["status"]
            )
        )
    if "evaluation_method" in value:
        import capo_iot_events.types.evaluation_method

        out["evaluationMethod"] = (
            capo_iot_events.types.evaluation_method.serialize_json(
                value["evaluation_method"]
            )
        )
    return out


def deserialize_json(data: dict) -> DetectorModelVersionSummary:
    out: DetectorModelVersionSummary = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    if "detectorModelVersion" in data:
        out["detector_model_version"] = data["detectorModelVersion"]
    if "detectorModelArn" in data:
        out["detector_model_arn"] = data["detectorModelArn"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "creationTime" in data:
        import capo_iot_events.types.timestamp

        out["creation_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import capo_iot_events.types.timestamp

        out["last_update_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    if "status" in data:
        import capo_iot_events.types.detector_model_version_status

        out["status"] = (
            capo_iot_events.types.detector_model_version_status.deserialize_json(
                data["status"]
            )
        )
    if "evaluationMethod" in data:
        import capo_iot_events.types.evaluation_method

        out["evaluation_method"] = (
            capo_iot_events.types.evaluation_method.deserialize_json(
                data["evaluationMethod"]
            )
        )
    return out

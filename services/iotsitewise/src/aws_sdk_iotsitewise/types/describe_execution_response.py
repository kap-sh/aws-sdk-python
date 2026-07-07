"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.execution_details
    import aws_sdk_iotsitewise.types.execution_result
    import aws_sdk_iotsitewise.types.execution_status
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.name
    import aws_sdk_iotsitewise.types.resolve_to
    import aws_sdk_iotsitewise.types.target_resource
    import aws_sdk_iotsitewise.types.timestamp
    import aws_sdk_iotsitewise.types.version


class DescribeExecutionResponse(TypedDict, closed=True):
    execution_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the execution.</p>"""
    action_type: NotRequired["aws_sdk_iotsitewise.types.name.Name"]
    """<p>The type of action exectued.</p>"""
    target_resource: "aws_sdk_iotsitewise.types.target_resource.TargetResource"
    target_resource_version: "aws_sdk_iotsitewise.types.version.Version"
    """<p>The version of the target resource.</p>"""
    resolve_to: NotRequired["aws_sdk_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this execution resolves to.</p>"""
    execution_start_time: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the process started.</p>"""
    execution_end_time: NotRequired["aws_sdk_iotsitewise.types.timestamp.Timestamp"]
    """<p>The time the process ended.</p>"""
    execution_status: "aws_sdk_iotsitewise.types.execution_status.ExecutionStatus"
    """<p>The status of the execution process.</p>"""
    execution_result: NotRequired[
        "aws_sdk_iotsitewise.types.execution_result.ExecutionResult"
    ]
    """<p>The result of the execution.</p>"""
    execution_details: NotRequired[
        "aws_sdk_iotsitewise.types.execution_details.ExecutionDetails"
    ]
    """<p>Provides detailed information about the execution of your anomaly detection models. This includes model metrics and training timestamps for both training and inference actions.</p> <ul> <li> <p> The training action (Amazon Web Services/ANOMALY_DETECTION_TRAINING), includes performance metrics that help you compare different versions of your anomaly detection models. These metrics provide insights into the model's performance during the training process. </p> </li> <li> <p> The inference action (Amazon Web Services/ANOMALY_DETECTION_INFERENCE), includes information about the results of executing your anomaly detection models. This helps you understand the output of your models and assess their performance. </p> </li> </ul>"""
    execution_entity_version: NotRequired["aws_sdk_iotsitewise.types.version.Version"]
    """<p>Entity version used for the execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeExecutionResponse) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    import aws_sdk_iotsitewise.types.target_resource

    out["targetResource"] = aws_sdk_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["targetResourceVersion"] = value["target_resource_version"]
    if "resolve_to" in value:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolveTo"] = aws_sdk_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    import aws_sdk_iotsitewise.types.timestamp

    out["executionStartTime"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["execution_start_time"]
    )
    if "execution_end_time" in value:
        import aws_sdk_iotsitewise.types.timestamp

        out["executionEndTime"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
            value["execution_end_time"]
        )
    import aws_sdk_iotsitewise.types.execution_status

    out["executionStatus"] = aws_sdk_iotsitewise.types.execution_status.serialize_json(
        value["execution_status"]
    )
    if "execution_result" in value:
        import aws_sdk_iotsitewise.types.execution_result

        out["executionResult"] = (
            aws_sdk_iotsitewise.types.execution_result.serialize_json(
                value["execution_result"]
            )
        )
    if "execution_details" in value:
        import aws_sdk_iotsitewise.types.execution_details

        out["executionDetails"] = (
            aws_sdk_iotsitewise.types.execution_details.serialize_json(
                value["execution_details"]
            )
        )
    if "execution_entity_version" in value:
        out["executionEntityVersion"] = value["execution_entity_version"]
    return out


def deserialize_json(data: dict) -> DescribeExecutionResponse:
    out: DescribeExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("DescribeExecutionResponse.execution_id required")
    if "actionType" in data:
        out["action_type"] = data["actionType"]
    if "targetResource" in data:
        import aws_sdk_iotsitewise.types.target_resource

        out["target_resource"] = (
            aws_sdk_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("DescribeExecutionResponse.target_resource required")
    if "targetResourceVersion" in data:
        out["target_resource_version"] = data["targetResourceVersion"]
    else:
        raise DeserializationError(
            "DescribeExecutionResponse.target_resource_version required"
        )
    if "resolveTo" in data:
        import aws_sdk_iotsitewise.types.resolve_to

        out["resolve_to"] = aws_sdk_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    if "executionStartTime" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["execution_start_time"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["executionStartTime"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeExecutionResponse.execution_start_time required"
        )
    if "executionEndTime" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["execution_end_time"] = (
            aws_sdk_iotsitewise.types.timestamp.deserialize_json(
                data["executionEndTime"]
            )
        )
    if "executionStatus" in data:
        import aws_sdk_iotsitewise.types.execution_status

        out["execution_status"] = (
            aws_sdk_iotsitewise.types.execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeExecutionResponse.execution_status required"
        )
    if "executionResult" in data:
        import aws_sdk_iotsitewise.types.execution_result

        out["execution_result"] = (
            aws_sdk_iotsitewise.types.execution_result.deserialize_json(
                data["executionResult"]
            )
        )
    if "executionDetails" in data:
        import aws_sdk_iotsitewise.types.execution_details

        out["execution_details"] = (
            aws_sdk_iotsitewise.types.execution_details.deserialize_json(
                data["executionDetails"]
            )
        )
    if "executionEntityVersion" in data:
        out["execution_entity_version"] = data["executionEntityVersion"]
    return out

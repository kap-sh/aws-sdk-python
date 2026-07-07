"""Generated from Smithy shape ``com.amazonaws.comprehend#FlywheelIterationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.any_length_string
    import aws_sdk_comprehend.types.comprehend_flywheel_arn
    import aws_sdk_comprehend.types.comprehend_model_arn
    import aws_sdk_comprehend.types.flywheel_iteration_id
    import aws_sdk_comprehend.types.flywheel_iteration_status
    import aws_sdk_comprehend.types.flywheel_model_evaluation_metrics
    import aws_sdk_comprehend.types.s3_uri
    import aws_sdk_comprehend.types.timestamp


class FlywheelIterationProperties(TypedDict, closed=True):
    flywheel_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_flywheel_arn.ComprehendFlywheelArn"
    ]
    """<p></p>"""
    flywheel_iteration_id: NotRequired[
        "aws_sdk_comprehend.types.flywheel_iteration_id.FlywheelIterationId"
    ]
    """<p></p>"""
    creation_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The creation start time of the flywheel iteration.</p>"""
    end_time: NotRequired["aws_sdk_comprehend.types.timestamp.Timestamp"]
    """<p>The completion time of this flywheel iteration.</p>"""
    status: NotRequired[
        "aws_sdk_comprehend.types.flywheel_iteration_status.FlywheelIterationStatus"
    ]
    """<p>The status of the flywheel iteration.</p>"""
    message: NotRequired["aws_sdk_comprehend.types.any_length_string.AnyLengthString"]
    """<p>A description of the status of the flywheel iteration.</p>"""
    evaluated_model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the evaluated model associated with this flywheel iteration.</p>"""
    evaluated_model_metrics: NotRequired[
        "aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.FlywheelModelEvaluationMetrics"
    ]
    trained_model_arn: NotRequired[
        "aws_sdk_comprehend.types.comprehend_model_arn.ComprehendModelArn"
    ]
    """<p>The ARN of the trained model associated with this flywheel iteration.</p>"""
    trained_model_metrics: NotRequired[
        "aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.FlywheelModelEvaluationMetrics"
    ]
    """<p>The metrics associated with the trained model.</p>"""
    evaluation_manifest_s3_prefix: NotRequired["aws_sdk_comprehend.types.s3_uri.S3Uri"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlywheelIterationProperties) -> dict:
    out: dict = {}
    if "flywheel_arn" in value:
        out["FlywheelArn"] = value["flywheel_arn"]
    if "flywheel_iteration_id" in value:
        out["FlywheelIterationId"] = value["flywheel_iteration_id"]
    if "creation_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["CreationTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "end_time" in value:
        import aws_sdk_comprehend.types.timestamp

        out["EndTime"] = aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "status" in value:
        import aws_sdk_comprehend.types.flywheel_iteration_status

        out["Status"] = (
            aws_sdk_comprehend.types.flywheel_iteration_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "evaluated_model_arn" in value:
        out["EvaluatedModelArn"] = value["evaluated_model_arn"]
    if "evaluated_model_metrics" in value:
        import aws_sdk_comprehend.types.flywheel_model_evaluation_metrics

        out["EvaluatedModelMetrics"] = (
            aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.serialize_aws_json_1_1(
                value["evaluated_model_metrics"]
            )
        )
    if "trained_model_arn" in value:
        out["TrainedModelArn"] = value["trained_model_arn"]
    if "trained_model_metrics" in value:
        import aws_sdk_comprehend.types.flywheel_model_evaluation_metrics

        out["TrainedModelMetrics"] = (
            aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.serialize_aws_json_1_1(
                value["trained_model_metrics"]
            )
        )
    if "evaluation_manifest_s3_prefix" in value:
        out["EvaluationManifestS3Prefix"] = value["evaluation_manifest_s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlywheelIterationProperties:
    out: FlywheelIterationProperties = {}  # type: ignore[typeddict-item]
    if "FlywheelArn" in data:
        out["flywheel_arn"] = data["FlywheelArn"]
    if "FlywheelIterationId" in data:
        out["flywheel_iteration_id"] = data["FlywheelIterationId"]
    if "CreationTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["creation_time"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_comprehend.types.timestamp

        out["end_time"] = aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Status" in data:
        import aws_sdk_comprehend.types.flywheel_iteration_status

        out["status"] = (
            aws_sdk_comprehend.types.flywheel_iteration_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "EvaluatedModelArn" in data:
        out["evaluated_model_arn"] = data["EvaluatedModelArn"]
    if "EvaluatedModelMetrics" in data:
        import aws_sdk_comprehend.types.flywheel_model_evaluation_metrics

        out["evaluated_model_metrics"] = (
            aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.deserialize_aws_json_1_1(
                data["EvaluatedModelMetrics"]
            )
        )
    if "TrainedModelArn" in data:
        out["trained_model_arn"] = data["TrainedModelArn"]
    if "TrainedModelMetrics" in data:
        import aws_sdk_comprehend.types.flywheel_model_evaluation_metrics

        out["trained_model_metrics"] = (
            aws_sdk_comprehend.types.flywheel_model_evaluation_metrics.deserialize_aws_json_1_1(
                data["TrainedModelMetrics"]
            )
        )
    if "EvaluationManifestS3Prefix" in data:
        out["evaluation_manifest_s3_prefix"] = data["EvaluationManifestS3Prefix"]
    return out

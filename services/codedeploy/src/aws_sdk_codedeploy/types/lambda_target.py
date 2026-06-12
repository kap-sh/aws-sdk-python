"""Generated from Smithy shape ``com.amazonaws.codedeploy#LambdaTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.lambda_function_info
    import aws_sdk_codedeploy.types.lifecycle_event_list
    import aws_sdk_codedeploy.types.target_arn
    import aws_sdk_codedeploy.types.target_id
    import aws_sdk_codedeploy.types.target_status
    import aws_sdk_codedeploy.types.time


class LambdaTarget(TypedDict):
    deployment_id: NotRequired["aws_sdk_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    target_id: NotRequired["aws_sdk_codedeploy.types.target_id.TargetId"]
    """<p> The unique ID of a deployment target that has a type of <code>lambdaTarget</code>. </p>"""
    target_arn: NotRequired["aws_sdk_codedeploy.types.target_arn.TargetArn"]
    """<p> The Amazon Resource Name (ARN) of the target. </p>"""
    status: NotRequired["aws_sdk_codedeploy.types.target_status.TargetStatus"]
    """<p> The status an Lambda deployment's target Lambda function. </p>"""
    last_updated_at: NotRequired["aws_sdk_codedeploy.types.time.Time"]
    """<p> The date and time when the target Lambda function was updated by a deployment. </p>"""
    lifecycle_events: NotRequired[
        "aws_sdk_codedeploy.types.lifecycle_event_list.LifecycleEventList"
    ]
    """<p> The lifecycle events of the deployment to this target Lambda function. </p>"""
    lambda_function_info: NotRequired[
        "aws_sdk_codedeploy.types.lambda_function_info.LambdaFunctionInfo"
    ]
    """<p> A <code>LambdaFunctionInfo</code> object that describes a target Lambda function. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaTarget) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import aws_sdk_codedeploy.types.target_status

        out["status"] = aws_sdk_codedeploy.types.target_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "last_updated_at" in value:
        import aws_sdk_codedeploy.types.time

        out["lastUpdatedAt"] = aws_sdk_codedeploy.types.time.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "lifecycle_events" in value:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycleEvents"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.serialize_aws_json_1_1(
                value["lifecycle_events"]
            )
        )
    if "lambda_function_info" in value:
        import aws_sdk_codedeploy.types.lambda_function_info

        out["lambdaFunctionInfo"] = (
            aws_sdk_codedeploy.types.lambda_function_info.serialize_aws_json_1_1(
                value["lambda_function_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaTarget:
    out: LambdaTarget = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "status" in data:
        import aws_sdk_codedeploy.types.target_status

        out["status"] = aws_sdk_codedeploy.types.target_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_codedeploy.types.time

        out["last_updated_at"] = aws_sdk_codedeploy.types.time.deserialize_aws_json_1_1(
            data["lastUpdatedAt"]
        )
    if "lifecycleEvents" in data:
        import aws_sdk_codedeploy.types.lifecycle_event_list

        out["lifecycle_events"] = (
            aws_sdk_codedeploy.types.lifecycle_event_list.deserialize_aws_json_1_1(
                data["lifecycleEvents"]
            )
        )
    if "lambdaFunctionInfo" in data:
        import aws_sdk_codedeploy.types.lambda_function_info

        out["lambda_function_info"] = (
            aws_sdk_codedeploy.types.lambda_function_info.deserialize_aws_json_1_1(
                data["lambdaFunctionInfo"]
            )
        )
    return out

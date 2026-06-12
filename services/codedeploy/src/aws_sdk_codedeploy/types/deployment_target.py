"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.cloud_formation_target
    import aws_sdk_codedeploy.types.deployment_target_type
    import aws_sdk_codedeploy.types.ecs_target
    import aws_sdk_codedeploy.types.instance_target
    import aws_sdk_codedeploy.types.lambda_target


class DeploymentTarget(TypedDict):
    deployment_target_type: NotRequired[
        "aws_sdk_codedeploy.types.deployment_target_type.DeploymentTargetType"
    ]
    """<p>The deployment type that is specific to the deployment's compute platform or deployments initiated by a CloudFormation stack update.</p>"""
    instance_target: NotRequired[
        "aws_sdk_codedeploy.types.instance_target.InstanceTarget"
    ]
    """<p> Information about the target for a deployment that uses the EC2/On-premises compute platform. </p>"""
    lambda_target: NotRequired["aws_sdk_codedeploy.types.lambda_target.LambdaTarget"]
    """<p> Information about the target for a deployment that uses the Lambda compute platform. </p>"""
    ecs_target: NotRequired["aws_sdk_codedeploy.types.ecs_target.ECSTarget"]
    """<p> Information about the target for a deployment that uses the Amazon ECS compute platform. </p>"""
    cloud_formation_target: NotRequired[
        "aws_sdk_codedeploy.types.cloud_formation_target.CloudFormationTarget"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentTarget) -> dict:
    out: dict = {}
    if "deployment_target_type" in value:
        import aws_sdk_codedeploy.types.deployment_target_type

        out["deploymentTargetType"] = (
            aws_sdk_codedeploy.types.deployment_target_type.serialize_aws_json_1_1(
                value["deployment_target_type"]
            )
        )
    if "instance_target" in value:
        import aws_sdk_codedeploy.types.instance_target

        out["instanceTarget"] = (
            aws_sdk_codedeploy.types.instance_target.serialize_aws_json_1_1(
                value["instance_target"]
            )
        )
    if "lambda_target" in value:
        import aws_sdk_codedeploy.types.lambda_target

        out["lambdaTarget"] = (
            aws_sdk_codedeploy.types.lambda_target.serialize_aws_json_1_1(
                value["lambda_target"]
            )
        )
    if "ecs_target" in value:
        import aws_sdk_codedeploy.types.ecs_target

        out["ecsTarget"] = aws_sdk_codedeploy.types.ecs_target.serialize_aws_json_1_1(
            value["ecs_target"]
        )
    if "cloud_formation_target" in value:
        import aws_sdk_codedeploy.types.cloud_formation_target

        out["cloudFormationTarget"] = (
            aws_sdk_codedeploy.types.cloud_formation_target.serialize_aws_json_1_1(
                value["cloud_formation_target"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentTarget:
    out: DeploymentTarget = {}  # type: ignore[typeddict-item]
    if "deploymentTargetType" in data:
        import aws_sdk_codedeploy.types.deployment_target_type

        out["deployment_target_type"] = (
            aws_sdk_codedeploy.types.deployment_target_type.deserialize_aws_json_1_1(
                data["deploymentTargetType"]
            )
        )
    if "instanceTarget" in data:
        import aws_sdk_codedeploy.types.instance_target

        out["instance_target"] = (
            aws_sdk_codedeploy.types.instance_target.deserialize_aws_json_1_1(
                data["instanceTarget"]
            )
        )
    if "lambdaTarget" in data:
        import aws_sdk_codedeploy.types.lambda_target

        out["lambda_target"] = (
            aws_sdk_codedeploy.types.lambda_target.deserialize_aws_json_1_1(
                data["lambdaTarget"]
            )
        )
    if "ecsTarget" in data:
        import aws_sdk_codedeploy.types.ecs_target

        out["ecs_target"] = (
            aws_sdk_codedeploy.types.ecs_target.deserialize_aws_json_1_1(
                data["ecsTarget"]
            )
        )
    if "cloudFormationTarget" in data:
        import aws_sdk_codedeploy.types.cloud_formation_target

        out["cloud_formation_target"] = (
            aws_sdk_codedeploy.types.cloud_formation_target.deserialize_aws_json_1_1(
                data["cloudFormationTarget"]
            )
        )
    return out

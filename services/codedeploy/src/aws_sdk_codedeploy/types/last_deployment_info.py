"""Generated from Smithy shape ``com.amazonaws.codedeploy#LastDeploymentInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_id
    import aws_sdk_codedeploy.types.deployment_status
    import aws_sdk_codedeploy.types.timestamp


class LastDeploymentInfo(TypedDict):
    deployment_id: NotRequired["aws_sdk_codedeploy.types.deployment_id.DeploymentId"]
    """<p> The unique ID of a deployment. </p>"""
    status: NotRequired["aws_sdk_codedeploy.types.deployment_status.DeploymentStatus"]
    """<p>The status of the most recent deployment.</p>"""
    end_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the most recent deployment to the deployment group was complete.</p>"""
    create_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates when the most recent deployment to the deployment group started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastDeploymentInfo) -> dict:
    out: dict = {}
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "status" in value:
        import aws_sdk_codedeploy.types.deployment_status

        out["status"] = (
            aws_sdk_codedeploy.types.deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "end_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["endTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "create_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["createTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LastDeploymentInfo:
    out: LastDeploymentInfo = {}  # type: ignore[typeddict-item]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "status" in data:
        import aws_sdk_codedeploy.types.deployment_status

        out["status"] = (
            aws_sdk_codedeploy.types.deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "endTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["end_time"] = aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "createTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["create_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["createTime"]
            )
        )
    return out

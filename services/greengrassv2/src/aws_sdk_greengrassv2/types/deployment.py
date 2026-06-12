"""Generated from Smithy shape ``com.amazonaws.greengrassv2#Deployment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.deployment_status
    import aws_sdk_greengrassv2.types.is_latest_for_target
    import aws_sdk_greengrassv2.types.non_empty_string
    import aws_sdk_greengrassv2.types.target_arn
    import aws_sdk_greengrassv2.types.thing_group_arn
    import aws_sdk_greengrassv2.types.timestamp


class Deployment(TypedDict):
    target_arn: NotRequired["aws_sdk_greengrassv2.types.target_arn.TargetARN"]
    """<p>The <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> of the target IoT thing or thing group. When creating a subdeployment, the targetARN can only be a thing group.</p>"""
    revision_id: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The revision number of the deployment.</p>"""
    deployment_id: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the deployment.</p>"""
    deployment_name: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the deployment.</p>"""
    creation_timestamp: NotRequired["aws_sdk_greengrassv2.types.timestamp.Timestamp"]
    """<p>The time at which the deployment was created, expressed in ISO 8601 format.</p>"""
    deployment_status: NotRequired[
        "aws_sdk_greengrassv2.types.deployment_status.DeploymentStatus"
    ]
    """<p>The status of the deployment.</p>"""
    is_latest_for_target: (
        "aws_sdk_greengrassv2.types.is_latest_for_target.IsLatestForTarget"
    )
    """<p>Whether or not the deployment is the latest revision for its target.</p>"""
    parent_target_arn: NotRequired[
        "aws_sdk_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The parent deployment's target <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">ARN</a> within a subdeployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "deployment_id" in value:
        out["deploymentId"] = value["deployment_id"]
    if "deployment_name" in value:
        out["deploymentName"] = value["deployment_name"]
    if "creation_timestamp" in value:
        import aws_sdk_greengrassv2.types.timestamp

        out["creationTimestamp"] = aws_sdk_greengrassv2.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "deployment_status" in value:
        import aws_sdk_greengrassv2.types.deployment_status

        out["deploymentStatus"] = (
            aws_sdk_greengrassv2.types.deployment_status.serialize_json(
                value["deployment_status"]
            )
        )
    out["isLatestForTarget"] = value.get("is_latest_for_target", False)
    if "parent_target_arn" in value:
        out["parentTargetArn"] = value["parent_target_arn"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "targetArn" in data:
        out["target_arn"] = data["targetArn"]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "deploymentId" in data:
        out["deployment_id"] = data["deploymentId"]
    if "deploymentName" in data:
        out["deployment_name"] = data["deploymentName"]
    if "creationTimestamp" in data:
        import aws_sdk_greengrassv2.types.timestamp

        out["creation_timestamp"] = (
            aws_sdk_greengrassv2.types.timestamp.deserialize_json(
                data["creationTimestamp"]
            )
        )
    if "deploymentStatus" in data:
        import aws_sdk_greengrassv2.types.deployment_status

        out["deployment_status"] = (
            aws_sdk_greengrassv2.types.deployment_status.deserialize_json(
                data["deploymentStatus"]
            )
        )
    if "isLatestForTarget" in data:
        out["is_latest_for_target"] = data["isLatestForTarget"]
    else:
        out["is_latest_for_target"] = False
    if "parentTargetArn" in data:
        out["parent_target_arn"] = data["parentTargetArn"]
    return out

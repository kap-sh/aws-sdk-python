"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.arn
    import capo_iotthingsgraph.types.deployment_target
    import capo_iotthingsgraph.types.greengrass_group_id
    import capo_iotthingsgraph.types.greengrass_group_version_id
    import capo_iotthingsgraph.types.group_name
    import capo_iotthingsgraph.types.system_instance_deployment_status
    import capo_iotthingsgraph.types.timestamp
    import capo_iotthingsgraph.types.urn


class SystemInstanceSummary(TypedDict, closed=True):
    id: NotRequired["capo_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the system instance.</p>"""
    arn: NotRequired["capo_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the system instance.</p>"""
    status: NotRequired[
        "capo_iotthingsgraph.types.system_instance_deployment_status.SystemInstanceDeploymentStatus"
    ]
    """<p>The status of the system instance.</p>"""
    target: NotRequired["capo_iotthingsgraph.types.deployment_target.DeploymentTarget"]
    """<p>The target of the system instance.</p>"""
    greengrass_group_name: NotRequired["capo_iotthingsgraph.types.group_name.GroupName"]
    """<p>The ID of the Greengrass group where the system instance is deployed.</p>"""
    created_at: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date when the system instance was created.</p>"""
    updated_at: NotRequired["capo_iotthingsgraph.types.timestamp.Timestamp"]
    """<p> The date and time when the system instance was last updated.</p>"""
    greengrass_group_id: NotRequired[
        "capo_iotthingsgraph.types.greengrass_group_id.GreengrassGroupId"
    ]
    """<p>The ID of the Greengrass group where the system instance is deployed.</p>"""
    greengrass_group_version_id: NotRequired[
        "capo_iotthingsgraph.types.greengrass_group_version_id.GreengrassGroupVersionId"
    ]
    """<p>The version of the Greengrass group where the system instance is deployed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemInstanceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import capo_iotthingsgraph.types.system_instance_deployment_status

        out["status"] = (
            capo_iotthingsgraph.types.system_instance_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "target" in value:
        import capo_iotthingsgraph.types.deployment_target

        out["target"] = (
            capo_iotthingsgraph.types.deployment_target.serialize_aws_json_1_1(
                value["target"]
            )
        )
    if "greengrass_group_name" in value:
        out["greengrassGroupName"] = value["greengrass_group_name"]
    if "created_at" in value:
        import capo_iotthingsgraph.types.timestamp

        out["createdAt"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_iotthingsgraph.types.timestamp

        out["updatedAt"] = capo_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "greengrass_group_id" in value:
        out["greengrassGroupId"] = value["greengrass_group_id"]
    if "greengrass_group_version_id" in value:
        out["greengrassGroupVersionId"] = value["greengrass_group_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemInstanceSummary:
    out: SystemInstanceSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import capo_iotthingsgraph.types.system_instance_deployment_status

        out["status"] = (
            capo_iotthingsgraph.types.system_instance_deployment_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "target" in data:
        import capo_iotthingsgraph.types.deployment_target

        out["target"] = (
            capo_iotthingsgraph.types.deployment_target.deserialize_aws_json_1_1(
                data["target"]
            )
        )
    if "greengrassGroupName" in data:
        out["greengrass_group_name"] = data["greengrassGroupName"]
    if "createdAt" in data:
        import capo_iotthingsgraph.types.timestamp

        out["created_at"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_iotthingsgraph.types.timestamp

        out["updated_at"] = (
            capo_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["updatedAt"]
            )
        )
    if "greengrassGroupId" in data:
        out["greengrass_group_id"] = data["greengrassGroupId"]
    if "greengrassGroupVersionId" in data:
        out["greengrass_group_version_id"] = data["greengrassGroupVersionId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.codedeploy#GenericRevisionInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.deployment_groups_list
    import aws_sdk_codedeploy.types.description
    import aws_sdk_codedeploy.types.timestamp


class GenericRevisionInfo(TypedDict):
    description: NotRequired["aws_sdk_codedeploy.types.description.Description"]
    """<p>A comment about the revision.</p>"""
    deployment_groups: NotRequired[
        "aws_sdk_codedeploy.types.deployment_groups_list.DeploymentGroupsList"
    ]
    """<p>The deployment groups for which this is the current target revision.</p>"""
    first_used_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was first used by CodeDeploy.</p>"""
    last_used_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was last used by CodeDeploy.</p>"""
    register_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>When the revision was registered with CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenericRevisionInfo) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "deployment_groups" in value:
        import aws_sdk_codedeploy.types.deployment_groups_list

        out["deploymentGroups"] = (
            aws_sdk_codedeploy.types.deployment_groups_list.serialize_aws_json_1_1(
                value["deployment_groups"]
            )
        )
    if "first_used_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["firstUsedTime"] = (
            aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
                value["first_used_time"]
            )
        )
    if "last_used_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["lastUsedTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["last_used_time"]
        )
    if "register_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["registerTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["register_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GenericRevisionInfo:
    out: GenericRevisionInfo = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "deploymentGroups" in data:
        import aws_sdk_codedeploy.types.deployment_groups_list

        out["deployment_groups"] = (
            aws_sdk_codedeploy.types.deployment_groups_list.deserialize_aws_json_1_1(
                data["deploymentGroups"]
            )
        )
    if "firstUsedTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["first_used_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["firstUsedTime"]
            )
        )
    if "lastUsedTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["last_used_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["lastUsedTime"]
            )
        )
    if "registerTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["register_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["registerTime"]
            )
        )
    return out

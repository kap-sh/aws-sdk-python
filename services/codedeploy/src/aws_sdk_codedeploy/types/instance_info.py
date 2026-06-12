"""Generated from Smithy shape ``com.amazonaws.codedeploy#InstanceInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.iam_session_arn
    import aws_sdk_codedeploy.types.iam_user_arn
    import aws_sdk_codedeploy.types.instance_arn
    import aws_sdk_codedeploy.types.instance_name
    import aws_sdk_codedeploy.types.tag_list
    import aws_sdk_codedeploy.types.timestamp


class InstanceInfo(TypedDict):
    instance_name: NotRequired["aws_sdk_codedeploy.types.instance_name.InstanceName"]
    """<p>The name of the on-premises instance.</p>"""
    iam_session_arn: NotRequired[
        "aws_sdk_codedeploy.types.iam_session_arn.IamSessionArn"
    ]
    """<p>The ARN of the IAM session associated with the on-premises instance.</p>"""
    iam_user_arn: NotRequired["aws_sdk_codedeploy.types.iam_user_arn.IamUserArn"]
    """<p>The user ARN associated with the on-premises instance.</p>"""
    instance_arn: NotRequired["aws_sdk_codedeploy.types.instance_arn.InstanceArn"]
    """<p>The ARN of the on-premises instance.</p>"""
    register_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>The time at which the on-premises instance was registered.</p>"""
    deregister_time: NotRequired["aws_sdk_codedeploy.types.timestamp.Timestamp"]
    """<p>If the on-premises instance was deregistered, the time at which the on-premises instance was deregistered.</p>"""
    tags: NotRequired["aws_sdk_codedeploy.types.tag_list.TagList"]
    """<p>The tags currently associated with the on-premises instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceInfo) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "iam_session_arn" in value:
        out["iamSessionArn"] = value["iam_session_arn"]
    if "iam_user_arn" in value:
        out["iamUserArn"] = value["iam_user_arn"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "register_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["registerTime"] = aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
            value["register_time"]
        )
    if "deregister_time" in value:
        import aws_sdk_codedeploy.types.timestamp

        out["deregisterTime"] = (
            aws_sdk_codedeploy.types.timestamp.serialize_aws_json_1_1(
                value["deregister_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceInfo:
    out: InstanceInfo = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "iamSessionArn" in data:
        out["iam_session_arn"] = data["iamSessionArn"]
    if "iamUserArn" in data:
        out["iam_user_arn"] = data["iamUserArn"]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "registerTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["register_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["registerTime"]
            )
        )
    if "deregisterTime" in data:
        import aws_sdk_codedeploy.types.timestamp

        out["deregister_time"] = (
            aws_sdk_codedeploy.types.timestamp.deserialize_aws_json_1_1(
                data["deregisterTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_codedeploy.types.tag_list

        out["tags"] = aws_sdk_codedeploy.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out

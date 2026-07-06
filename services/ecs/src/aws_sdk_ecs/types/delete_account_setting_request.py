"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAccountSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting_name
    import aws_sdk_ecs.types.string


class DeleteAccountSettingRequest(TypedDict, closed=True):
    name: "aws_sdk_ecs.types.setting_name.SettingName"
    """<p>The resource name to disable the account setting for. If <code>serviceLongArnFormat</code> is specified, the ARN for your Amazon ECS services is affected. If <code>taskLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS tasks is affected. If <code>containerInstanceLongArnFormat</code> is specified, the ARN and resource ID for your Amazon ECS container instances is affected. If <code>awsvpcTrunking</code> is specified, the ENI limit for your Amazon ECS container instances is affected.</p>"""
    principal_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the principal. It can be a user, role, or the root user. If you specify the root user, it disables the account setting for all users, roles, and the root user of the account unless a user or role explicitly overrides these settings. If this field is omitted, the setting is changed only for the authenticated user.</p> <p>In order to use this parameter, you must be the root user, or the principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountSettingRequest) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.setting_name

    out["name"] = aws_sdk_ecs.types.setting_name.serialize_aws_json_1_1(value["name"])
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountSettingRequest:
    out: DeleteAccountSettingRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_ecs.types.setting_name

        out["name"] = aws_sdk_ecs.types.setting_name.deserialize_aws_json_1_1(
            data["name"]
        )
    else:
        raise DeserializationError("DeleteAccountSettingRequest.name required")
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    return out

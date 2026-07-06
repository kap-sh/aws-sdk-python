"""Generated from Smithy shape ``com.amazonaws.ecs#Setting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.setting_name
    import aws_sdk_ecs.types.setting_type
    import aws_sdk_ecs.types.string


class Setting(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ecs.types.setting_name.SettingName"]
    """<p>The Amazon ECS resource name.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Determines whether the account setting is on or off for the specified resource.</p>"""
    principal_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the principal. It can be a user, role, or the root user. If this field is omitted, the authenticated user is assumed.</p>"""
    type: NotRequired["aws_sdk_ecs.types.setting_type.SettingType"]
    """<p>Indicates whether Amazon Web Services manages the account setting, or if the user manages it.</p> <p> <code>aws_managed</code> account settings are read-only, as Amazon Web Services manages such on the customer's behalf. Currently, the <code>guardDutyActivate</code> account setting is the only one Amazon Web Services manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Setting) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_ecs.types.setting_name

        out["name"] = aws_sdk_ecs.types.setting_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "type" in value:
        import aws_sdk_ecs.types.setting_type

        out["type"] = aws_sdk_ecs.types.setting_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Setting:
    out: Setting = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_ecs.types.setting_name

        out["name"] = aws_sdk_ecs.types.setting_name.deserialize_aws_json_1_1(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    if "principalArn" in data:
        out["principal_arn"] = data["principalArn"]
    if "type" in data:
        import aws_sdk_ecs.types.setting_type

        out["type"] = aws_sdk_ecs.types.setting_type.deserialize_aws_json_1_1(
            data["type"]
        )
    return out

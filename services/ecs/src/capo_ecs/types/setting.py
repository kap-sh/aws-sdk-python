"""Generated from Smithy shape ``com.amazonaws.ecs#Setting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.setting_name
    import capo_ecs.types.setting_type
    import capo_ecs.types.string


class Setting(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.setting_name.SettingName"]
    """<p>The Amazon ECS resource name.</p>"""
    value: NotRequired["capo_ecs.types.string.String"]
    """<p>Determines whether the account setting is on or off for the specified resource.</p>"""
    principal_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The ARN of the principal. It can be a user, role, or the root user. If this field is omitted, the authenticated user is assumed.</p>"""
    type: NotRequired["capo_ecs.types.setting_type.SettingType"]
    """<p>Indicates whether Amazon Web Services manages the account setting, or if the user manages it.</p> <p> <code>aws_managed</code> account settings are read-only, as Amazon Web Services manages such on the customer's behalf. Currently, the <code>guardDutyActivate</code> account setting is the only one Amazon Web Services manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Setting) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_ecs.types.setting_name

        out["name"] = capo_ecs.types.setting_name.serialize_aws_json_1_1(value["name"])
    if "value" in value:
        out["value"] = value["value"]
    if "principal_arn" in value:
        out["principalArn"] = value["principal_arn"]
    if "type" in value:
        import capo_ecs.types.setting_type

        out["type"] = capo_ecs.types.setting_type.serialize_aws_json_1_1(value["type"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Setting:
    out: Setting = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_ecs.types.setting_name

        out["name"] = capo_ecs.types.setting_name.deserialize_aws_json_1_1(data["name"])
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    if data.get("type") is not None:
        import capo_ecs.types.setting_type

        out["type"] = capo_ecs.types.setting_type.deserialize_aws_json_1_1(data["type"])
    return out

"""Generated from Smithy shape ``com.amazonaws.workspaces#UserSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.maximum_length
    import capo_workspaces.types.user_setting_action_enum
    import capo_workspaces.types.user_setting_permission_enum


class UserSetting(TypedDict, closed=True):
    action: "capo_workspaces.types.user_setting_action_enum.UserSettingActionEnum"
    """<p>Indicates the type of action.</p>"""
    permission: (
        "capo_workspaces.types.user_setting_permission_enum.UserSettingPermissionEnum"
    )
    """<p>Indicates if the setting is enabled or disabled.</p>"""
    maximum_length: NotRequired["capo_workspaces.types.maximum_length.MaximumLength"]
    """<p>Indicates the maximum character length for the specified user setting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSetting) -> dict:
    out: dict = {}
    import capo_workspaces.types.user_setting_action_enum

    out["Action"] = (
        capo_workspaces.types.user_setting_action_enum.serialize_aws_json_1_1(
            value["action"]
        )
    )
    import capo_workspaces.types.user_setting_permission_enum

    out["Permission"] = (
        capo_workspaces.types.user_setting_permission_enum.serialize_aws_json_1_1(
            value["permission"]
        )
    )
    if "maximum_length" in value:
        out["MaximumLength"] = value["maximum_length"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserSetting:
    out: UserSetting = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import capo_workspaces.types.user_setting_action_enum

        out["action"] = (
            capo_workspaces.types.user_setting_action_enum.deserialize_aws_json_1_1(
                data["Action"]
            )
        )
    else:
        raise DeserializationError("UserSetting.action required")
    if "Permission" in data:
        import capo_workspaces.types.user_setting_permission_enum

        out["permission"] = (
            capo_workspaces.types.user_setting_permission_enum.deserialize_aws_json_1_1(
                data["Permission"]
            )
        )
    else:
        raise DeserializationError("UserSetting.permission required")
    if "MaximumLength" in data:
        out["maximum_length"] = data["MaximumLength"]
    return out

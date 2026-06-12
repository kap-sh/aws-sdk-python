"""Generated from Smithy shape ``com.amazonaws.appstream#UserSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.action
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.permission


class UserSetting(TypedDict):
    action: NotRequired["aws_sdk_appstream.types.action.Action"]
    """<p>The action that is enabled or disabled.</p>"""
    permission: NotRequired["aws_sdk_appstream.types.permission.Permission"]
    """<p>Indicates whether the action is enabled or disabled.</p>"""
    maximum_length: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>Specifies the number of characters that can be copied by end users from the local device to the remote session, and to the local device from the remote session.</p> <p>This can be specified only for the <code>CLIPBOARD_COPY_FROM_LOCAL_DEVICE</code> and <code>CLIPBOARD_COPY_TO_LOCAL_DEVICE</code> actions.</p> <p>This defaults to 20,971,520 (20 MB) when unspecified and the permission is <code>ENABLED</code>. This can't be specified when the permission is <code>DISABLED</code>. </p> <p>The value can be between 1 and 20,971,520 (20 MB).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSetting) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_appstream.types.action

        out["Action"] = aws_sdk_appstream.types.action.serialize_aws_json_1_1(
            value["action"]
        )
    if "permission" in value:
        import aws_sdk_appstream.types.permission

        out["Permission"] = aws_sdk_appstream.types.permission.serialize_aws_json_1_1(
            value["permission"]
        )
    if "maximum_length" in value:
        out["MaximumLength"] = value["maximum_length"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserSetting:
    out: UserSetting = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_appstream.types.action

        out["action"] = aws_sdk_appstream.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if "Permission" in data:
        import aws_sdk_appstream.types.permission

        out["permission"] = aws_sdk_appstream.types.permission.deserialize_aws_json_1_1(
            data["Permission"]
        )
    if "MaximumLength" in data:
        out["maximum_length"] = data["MaximumLength"]
    return out

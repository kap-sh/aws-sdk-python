"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentRunWith``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.non_empty_string
    import aws_sdk_greengrassv2.types.system_resource_limits


class ComponentRunWith(TypedDict):
    posix_user: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The POSIX system user and, optionally, group to use to run this component on Linux core devices. The user, and group if specified, must exist on each Linux core device. Specify the user and group separated by a colon (<code>:</code>) in the following format: <code>user:group</code>. The group is optional. If you don't specify a group, the IoT Greengrass Core software uses the primary user for the group.</p> <p>If you omit this parameter, the IoT Greengrass Core software uses the default system user and group that you configure on the Greengrass nucleus component. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user\">Configure the user and group that run components</a>.</p>"""
    system_resource_limits: NotRequired[
        "aws_sdk_greengrassv2.types.system_resource_limits.SystemResourceLimits"
    ]
    r"""<p>The system resource limits to apply to this component's process on the core device. IoT Greengrass currently supports this feature on only Linux core devices.</p> <p>If you omit this parameter, the IoT Greengrass Core software uses the default system resource limits that you configure on the Greengrass nucleus component. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-system-resource-limits\">Configure system resource limits for components</a>.</p>"""
    windows_user: NotRequired[
        "aws_sdk_greengrassv2.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The Windows user to use to run this component on Windows core devices. The user must exist on each Windows core device, and its name and password must be in the LocalSystem account's Credentials Manager instance.</p> <p>If you omit this parameter, the IoT Greengrass Core software uses the default Windows user that you configure on the Greengrass nucleus component. For more information, see <a href=\"https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#configure-component-user\">Configure the user and group that run components</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentRunWith) -> dict:
    out: dict = {}
    if "posix_user" in value:
        out["posixUser"] = value["posix_user"]
    if "system_resource_limits" in value:
        import aws_sdk_greengrassv2.types.system_resource_limits

        out["systemResourceLimits"] = (
            aws_sdk_greengrassv2.types.system_resource_limits.serialize_json(
                value["system_resource_limits"]
            )
        )
    if "windows_user" in value:
        out["windowsUser"] = value["windows_user"]
    return out


def deserialize_json(data: dict) -> ComponentRunWith:
    out: ComponentRunWith = {}  # type: ignore[typeddict-item]
    if "posixUser" in data:
        out["posix_user"] = data["posixUser"]
    if "systemResourceLimits" in data:
        import aws_sdk_greengrassv2.types.system_resource_limits

        out["system_resource_limits"] = (
            aws_sdk_greengrassv2.types.system_resource_limits.deserialize_json(
                data["systemResourceLimits"]
            )
        )
    if "windowsUser" in data:
        out["windows_user"] = data["windowsUser"]
    return out

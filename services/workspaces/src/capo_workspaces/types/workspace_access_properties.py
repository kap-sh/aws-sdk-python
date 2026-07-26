"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceAccessProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.access_endpoint_config
    import capo_workspaces.types.access_property_value


class WorkspaceAccessProperties(TypedDict, closed=True):
    device_type_windows: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Windows clients to access their WorkSpaces.</p>"""
    device_type_osx: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use macOS clients to access their WorkSpaces.</p>"""
    device_type_web: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can access their WorkSpaces through a web browser.</p>"""
    device_type_ios: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use iOS devices to access their WorkSpaces.</p>"""
    device_type_android: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Android and Android-compatible Chrome OS devices to access their WorkSpaces.</p>"""
    device_type_chrome_os: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Chromebooks to access their WorkSpaces.</p>"""
    device_type_zero_client: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use zero client devices to access their WorkSpaces.</p>"""
    device_type_linux: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Linux clients to access their WorkSpaces.</p>"""
    device_type_work_spaces_thin_client: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can access their WorkSpaces through a WorkSpaces Thin Client.</p>"""
    access_endpoint_config: NotRequired[
        "capo_workspaces.types.access_endpoint_config.AccessEndpointConfig"
    ]
    """<p>Specifies the configuration for accessing the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceAccessProperties) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeIos"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_chrome_os" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeChromeOs"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_chrome_os"]
            )
        )
    if "device_type_zero_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeZeroClient"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_zero_client"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_work_spaces_thin_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWorkSpacesThinClient"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_work_spaces_thin_client"]
            )
        )
    if "access_endpoint_config" in value:
        import capo_workspaces.types.access_endpoint_config

        out["AccessEndpointConfig"] = (
            capo_workspaces.types.access_endpoint_config.serialize_aws_json_1_1(
                value["access_endpoint_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceAccessProperties:
    out: WorkspaceAccessProperties = {}  # type: ignore[typeddict-item]
    if "DeviceTypeWindows" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_windows"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if "DeviceTypeOsx" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_osx"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if "DeviceTypeWeb" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_web"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    if "DeviceTypeIos" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_ios"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if "DeviceTypeAndroid" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_android"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if "DeviceTypeChromeOs" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_chrome_os"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeChromeOs"]
            )
        )
    if "DeviceTypeZeroClient" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_zero_client"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeZeroClient"]
            )
        )
    if "DeviceTypeLinux" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_linux"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if "DeviceTypeWorkSpacesThinClient" in data:
        import capo_workspaces.types.access_property_value

        out["device_type_work_spaces_thin_client"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWorkSpacesThinClient"]
            )
        )
    if "AccessEndpointConfig" in data:
        import capo_workspaces.types.access_endpoint_config

        out["access_endpoint_config"] = (
            capo_workspaces.types.access_endpoint_config.deserialize_aws_json_1_1(
                data["AccessEndpointConfig"]
            )
        )
    return out

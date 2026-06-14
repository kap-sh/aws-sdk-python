"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportClientBrandingResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.default_client_branding_attributes
    import aws_sdk_workspaces.types.ios_client_branding_attributes


class ImportClientBrandingResult(TypedDict):
    device_type_windows: NotRequired[
        "aws_sdk_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Windows devices.</p>"""
    device_type_osx: NotRequired[
        "aws_sdk_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for macOS devices.</p>"""
    device_type_android: NotRequired[
        "aws_sdk_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Android devices.</p>"""
    device_type_ios: NotRequired[
        "aws_sdk_workspaces.types.ios_client_branding_attributes.IosClientBrandingAttributes"
    ]
    """<p>The branding information configured for iOS devices.</p>"""
    device_type_linux: NotRequired[
        "aws_sdk_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Linux devices.</p>"""
    device_type_web: NotRequired[
        "aws_sdk_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for web access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportClientBrandingResult) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWindows"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["DeviceTypeOsx"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_android" in value:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["DeviceTypeAndroid"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_ios" in value:
        import aws_sdk_workspaces.types.ios_client_branding_attributes

        out["DeviceTypeIos"] = (
            aws_sdk_workspaces.types.ios_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_linux" in value:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["DeviceTypeLinux"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_web" in value:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWeb"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportClientBrandingResult:
    out: ImportClientBrandingResult = {}  # type: ignore[typeddict-item]
    if "DeviceTypeWindows" in data:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["device_type_windows"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if "DeviceTypeOsx" in data:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["device_type_osx"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if "DeviceTypeAndroid" in data:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["device_type_android"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if "DeviceTypeIos" in data:
        import aws_sdk_workspaces.types.ios_client_branding_attributes

        out["device_type_ios"] = (
            aws_sdk_workspaces.types.ios_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if "DeviceTypeLinux" in data:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["device_type_linux"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if "DeviceTypeWeb" in data:
        import aws_sdk_workspaces.types.default_client_branding_attributes

        out["device_type_web"] = (
            aws_sdk_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    return out

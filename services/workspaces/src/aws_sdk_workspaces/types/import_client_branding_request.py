"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportClientBrandingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.default_import_client_branding_attributes
    import aws_sdk_workspaces.types.directory_id
    import aws_sdk_workspaces.types.ios_import_client_branding_attributes


class ImportClientBrandingRequest(TypedDict):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier of the WorkSpace for which you want to import client branding.</p>"""
    device_type_windows: NotRequired[
        "aws_sdk_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Windows devices.</p>"""
    device_type_osx: NotRequired[
        "aws_sdk_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for macOS devices.</p>"""
    device_type_android: NotRequired[
        "aws_sdk_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Android devices.</p>"""
    device_type_ios: NotRequired[
        "aws_sdk_workspaces.types.ios_import_client_branding_attributes.IosImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for iOS devices.</p>"""
    device_type_linux: NotRequired[
        "aws_sdk_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Linux devices.</p>"""
    device_type_web: NotRequired[
        "aws_sdk_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for web access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportClientBrandingRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "device_type_windows" in value:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeWindows"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeOsx"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_android" in value:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeAndroid"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_ios" in value:
        import aws_sdk_workspaces.types.ios_import_client_branding_attributes

        out["DeviceTypeIos"] = (
            aws_sdk_workspaces.types.ios_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_linux" in value:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeLinux"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_web" in value:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeWeb"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportClientBrandingRequest:
    out: ImportClientBrandingRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ImportClientBrandingRequest.resource_id required")
    if "DeviceTypeWindows" in data:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["device_type_windows"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if "DeviceTypeOsx" in data:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["device_type_osx"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if "DeviceTypeAndroid" in data:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["device_type_android"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if "DeviceTypeIos" in data:
        import aws_sdk_workspaces.types.ios_import_client_branding_attributes

        out["device_type_ios"] = (
            aws_sdk_workspaces.types.ios_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if "DeviceTypeLinux" in data:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["device_type_linux"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if "DeviceTypeWeb" in data:
        import aws_sdk_workspaces.types.default_import_client_branding_attributes

        out["device_type_web"] = (
            aws_sdk_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    return out

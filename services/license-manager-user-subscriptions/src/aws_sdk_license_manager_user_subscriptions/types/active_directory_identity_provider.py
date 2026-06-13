"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ActiveDirectoryIdentityProvider``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.active_directory_settings
    import aws_sdk_license_manager_user_subscriptions.types.active_directory_type
    import aws_sdk_license_manager_user_subscriptions.types.directory


class ActiveDirectoryIdentityProvider(TypedDict):
    directory_id: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.directory.Directory"
    ]
    """<p>The directory ID for an Active Directory identity provider.</p>"""
    active_directory_settings: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.active_directory_settings.ActiveDirectorySettings"
    ]
    """<p>The <code>ActiveDirectorySettings</code> resource contains details about the Active Directory, including network access details such as domain name and IP addresses, and the credential provider for user administration.</p>"""
    active_directory_type: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.active_directory_type.ActiveDirectoryType"
    ]
    """<p>The type of Active Directory – either a self-managed Active Directory or an Amazon Web Services Managed Active Directory.</p>"""
    is_shared_active_directory: NotRequired["bool"]
    """<p>Whether this directory is shared from an Amazon Web Services Managed Active Directory. The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveDirectoryIdentityProvider) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "active_directory_settings" in value:
        import aws_sdk_license_manager_user_subscriptions.types.active_directory_settings

        out["ActiveDirectorySettings"] = (
            aws_sdk_license_manager_user_subscriptions.types.active_directory_settings.serialize_json(
                value["active_directory_settings"]
            )
        )
    if "active_directory_type" in value:
        out["ActiveDirectoryType"] = value["active_directory_type"]
    if "is_shared_active_directory" in value:
        out["IsSharedActiveDirectory"] = value["is_shared_active_directory"]
    return out


def deserialize_json(data: dict) -> ActiveDirectoryIdentityProvider:
    out: ActiveDirectoryIdentityProvider = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    if "ActiveDirectorySettings" in data:
        import aws_sdk_license_manager_user_subscriptions.types.active_directory_settings

        out["active_directory_settings"] = (
            aws_sdk_license_manager_user_subscriptions.types.active_directory_settings.deserialize_json(
                data["ActiveDirectorySettings"]
            )
        )
    if "ActiveDirectoryType" in data:
        out["active_directory_type"] = data["ActiveDirectoryType"]
    if "IsSharedActiveDirectory" in data:
        out["is_shared_active_directory"] = data["IsSharedActiveDirectory"]
    return out

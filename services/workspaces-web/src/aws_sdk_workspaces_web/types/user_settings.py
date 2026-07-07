"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UserSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.branding_configuration
    import aws_sdk_workspaces_web.types.cookie_synchronization_configuration
    import aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes
    import aws_sdk_workspaces_web.types.enabled_type
    import aws_sdk_workspaces_web.types.encryption_context_map
    import aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes
    import aws_sdk_workspaces_web.types.key_arn
    import aws_sdk_workspaces_web.types.toolbar_configuration


class UserSettings(TypedDict, closed=True):
    user_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this user settings is associated with.</p>"""
    copy_allowed: NotRequired["aws_sdk_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can copy text from the streaming session to the local device.</p>"""
    paste_allowed: NotRequired["aws_sdk_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can paste text from the local device to the streaming session.</p>"""
    download_allowed: NotRequired[
        "aws_sdk_workspaces_web.types.enabled_type.EnabledType"
    ]
    """<p>Specifies whether the user can download files from the streaming session to the local device.</p>"""
    upload_allowed: NotRequired["aws_sdk_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can upload files from the local device to the streaming session.</p>"""
    print_allowed: NotRequired["aws_sdk_workspaces_web.types.enabled_type.EnabledType"]
    """<p>Specifies whether the user can print to the local device.</p>"""
    disconnect_timeout_in_minutes: NotRequired[
        "aws_sdk_workspaces_web.types.disconnect_timeout_in_minutes.DisconnectTimeoutInMinutes"
    ]
    """<p>The amount of time that a streaming session remains active after users disconnect.</p>"""
    idle_disconnect_timeout_in_minutes: NotRequired[
        "aws_sdk_workspaces_web.types.idle_disconnect_timeout_in_minutes.IdleDisconnectTimeoutInMinutes"
    ]
    """<p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.</p>"""
    cookie_synchronization_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.cookie_synchronization_configuration.CookieSynchronizationConfiguration"
    ]
    """<p>The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.</p>"""
    customer_managed_key: NotRequired["aws_sdk_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the user settings.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the user settings.</p>"""
    deep_link_allowed: NotRequired[
        "aws_sdk_workspaces_web.types.enabled_type.EnabledType"
    ]
    """<p>Specifies whether the user can use deep links that open automatically when connecting to a session.</p>"""
    toolbar_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.toolbar_configuration.ToolbarConfiguration"
    ]
    """<p>The configuration of the toolbar. This allows administrators to select the toolbar type and visual mode, set maximum display resolution for sessions, and choose which items are visible to end users during their sessions. If administrators do not modify these settings, end users retain control over their toolbar preferences.</p>"""
    branding_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.branding_configuration.BrandingConfiguration"
    ]
    """<p>The branding configuration output that customizes the appearance of the web portal for end users.</p>"""
    web_authn_allowed: NotRequired[
        "aws_sdk_workspaces_web.types.enabled_type.EnabledType"
    ]
    """<p>Specifies whether the user can use WebAuthn redirection for passwordless login to websites within the streaming session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSettings) -> dict:
    out: dict = {}
    out["userSettingsArn"] = value["user_settings_arn"]
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "copy_allowed" in value:
        out["copyAllowed"] = value["copy_allowed"]
    if "paste_allowed" in value:
        out["pasteAllowed"] = value["paste_allowed"]
    if "download_allowed" in value:
        out["downloadAllowed"] = value["download_allowed"]
    if "upload_allowed" in value:
        out["uploadAllowed"] = value["upload_allowed"]
    if "print_allowed" in value:
        out["printAllowed"] = value["print_allowed"]
    if "disconnect_timeout_in_minutes" in value:
        out["disconnectTimeoutInMinutes"] = value["disconnect_timeout_in_minutes"]
    if "idle_disconnect_timeout_in_minutes" in value:
        out["idleDisconnectTimeoutInMinutes"] = value[
            "idle_disconnect_timeout_in_minutes"
        ]
    if "cookie_synchronization_configuration" in value:
        import aws_sdk_workspaces_web.types.cookie_synchronization_configuration

        out["cookieSynchronizationConfiguration"] = (
            aws_sdk_workspaces_web.types.cookie_synchronization_configuration.serialize_json(
                value["cookie_synchronization_configuration"]
            )
        )
    if "customer_managed_key" in value:
        out["customerManagedKey"] = value["customer_managed_key"]
    if "additional_encryption_context" in value:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additionalEncryptionContext"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.serialize_json(
                value["additional_encryption_context"]
            )
        )
    if "deep_link_allowed" in value:
        out["deepLinkAllowed"] = value["deep_link_allowed"]
    if "toolbar_configuration" in value:
        import aws_sdk_workspaces_web.types.toolbar_configuration

        out["toolbarConfiguration"] = (
            aws_sdk_workspaces_web.types.toolbar_configuration.serialize_json(
                value["toolbar_configuration"]
            )
        )
    if "branding_configuration" in value:
        import aws_sdk_workspaces_web.types.branding_configuration

        out["brandingConfiguration"] = (
            aws_sdk_workspaces_web.types.branding_configuration.serialize_json(
                value["branding_configuration"]
            )
        )
    if "web_authn_allowed" in value:
        out["webAuthnAllowed"] = value["web_authn_allowed"]
    return out


def deserialize_json(data: dict) -> UserSettings:
    out: UserSettings = {}  # type: ignore[typeddict-item]
    if "userSettingsArn" in data:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        raise DeserializationError("UserSettings.user_settings_arn required")
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "copyAllowed" in data:
        out["copy_allowed"] = data["copyAllowed"]
    if "pasteAllowed" in data:
        out["paste_allowed"] = data["pasteAllowed"]
    if "downloadAllowed" in data:
        out["download_allowed"] = data["downloadAllowed"]
    if "uploadAllowed" in data:
        out["upload_allowed"] = data["uploadAllowed"]
    if "printAllowed" in data:
        out["print_allowed"] = data["printAllowed"]
    if "disconnectTimeoutInMinutes" in data:
        out["disconnect_timeout_in_minutes"] = data["disconnectTimeoutInMinutes"]
    if "idleDisconnectTimeoutInMinutes" in data:
        out["idle_disconnect_timeout_in_minutes"] = data[
            "idleDisconnectTimeoutInMinutes"
        ]
    if "cookieSynchronizationConfiguration" in data:
        import aws_sdk_workspaces_web.types.cookie_synchronization_configuration

        out["cookie_synchronization_configuration"] = (
            aws_sdk_workspaces_web.types.cookie_synchronization_configuration.deserialize_json(
                data["cookieSynchronizationConfiguration"]
            )
        )
    if "customerManagedKey" in data:
        out["customer_managed_key"] = data["customerManagedKey"]
    if "additionalEncryptionContext" in data:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additional_encryption_context"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.deserialize_json(
                data["additionalEncryptionContext"]
            )
        )
    if "deepLinkAllowed" in data:
        out["deep_link_allowed"] = data["deepLinkAllowed"]
    if "toolbarConfiguration" in data:
        import aws_sdk_workspaces_web.types.toolbar_configuration

        out["toolbar_configuration"] = (
            aws_sdk_workspaces_web.types.toolbar_configuration.deserialize_json(
                data["toolbarConfiguration"]
            )
        )
    if "brandingConfiguration" in data:
        import aws_sdk_workspaces_web.types.branding_configuration

        out["branding_configuration"] = (
            aws_sdk_workspaces_web.types.branding_configuration.deserialize_json(
                data["brandingConfiguration"]
            )
        )
    if "webAuthnAllowed" in data:
        out["web_authn_allowed"] = data["webAuthnAllowed"]
    return out

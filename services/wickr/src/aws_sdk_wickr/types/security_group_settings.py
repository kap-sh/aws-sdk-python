"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.calling_settings
    import aws_sdk_wickr.types.password_requirements
    import aws_sdk_wickr.types.permitted_networks_list
    import aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list
    import aws_sdk_wickr.types.security_group_string_list
    import aws_sdk_wickr.types.shredder_settings
    import aws_sdk_wickr.types.wickr_aws_networks_list


class SecurityGroupSettings(TypedDict, closed=True):
    always_reauthenticate: NotRequired["bool"]
    """<p>Requires users to reauthenticate every time they return to the application, providing an additional layer of security.</p>"""
    atak_package_values: NotRequired[
        "aws_sdk_wickr.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>Configuration values for ATAK (Android Team Awareness Kit) package integration, when ATAK is enabled.</p>"""
    calling: NotRequired["aws_sdk_wickr.types.calling_settings.CallingSettings"]
    """<p>The calling feature permissions and settings that control what types of calls users can initiate and participate in.</p>"""
    check_for_updates: NotRequired["bool"]
    """<p>Enables automatic checking for Wickr client updates to ensure users stay current with the latest version.</p>"""
    enable_atak: NotRequired["bool"]
    """<p>Enables ATAK (Android Team Awareness Kit) integration for tactical communication and situational awareness.</p>"""
    enable_crash_reports: NotRequired["bool"]
    """<p>Allow users to report crashes.</p>"""
    enable_file_download: NotRequired["bool"]
    """<p>Specifies whether users can download files from messages to their devices.</p>"""
    enable_guest_federation: NotRequired["bool"]
    """<p>Allows users to communicate with guest users from other Wickr networks and federated external networks.</p>"""
    enable_notification_preview: NotRequired["bool"]
    """<p>Enables message preview text in push notifications, allowing users to see message content before opening the app.</p>"""
    enable_open_access_option: NotRequired["bool"]
    """<p> Allow users to avoid censorship when they are geo-blocked or have network limitations.</p>"""
    enable_restricted_global_federation: NotRequired["bool"]
    """<p>Enables restricted global federation, limiting external communication to only specified permitted networks.</p>"""
    files_enabled: NotRequired["bool"]
    """<p>Enables file sharing capabilities, allowing users to send and receive files in conversations.</p>"""
    force_device_lockout: NotRequired["int"]
    """<p> Defines the number of failed login attempts before data stored on the device is reset. Should be less than lockoutThreshold.</p>"""
    force_open_access: NotRequired["bool"]
    """<p>Automatically enable and enforce Wickr open access on all devices. Valid only if enableOpenAccessOption settings is enabled.</p>"""
    force_read_receipts: NotRequired["bool"]
    """<p>Allow user approved bots to read messages in rooms without using a slash command.</p>"""
    global_federation: NotRequired["bool"]
    """<p>Allows users to communicate with users on other Wickr instances (Wickr Enterprise) outside the current network.</p>"""
    is_ato_enabled: NotRequired["bool"]
    """<p>Enforces a two-factor authentication when a user adds a new device to their account.</p>"""
    is_link_preview_enabled: NotRequired["bool"]
    """<p>Enables automatic preview of links shared in messages, showing webpage thumbnails and descriptions.</p>"""
    location_allow_maps: NotRequired["bool"]
    """<p>Allows map integration in location sharing, enabling users to view shared locations on interactive maps. Only allowed when location setting is enabled.</p>"""
    location_enabled: NotRequired["bool"]
    """<p>Enables location sharing features, allowing users to share their current location with others.</p>"""
    max_auto_download_size: NotRequired["int"]
    """<p>The maximum file size in bytes that will be automatically downloaded without user confirmation. Only allowed if fileDownload is enabled. Valid Values [512000 (low_quality), 7340032 (high_quality) ]</p>"""
    max_bor: NotRequired["int"]
    """<p>The maximum burn-on-read (BOR) time in seconds, which determines how long messages remain visible before auto-deletion after being read.</p>"""
    max_ttl: NotRequired["int"]
    """<p>The maximum time-to-live (TTL) in seconds for messages, after which they will be automatically deleted from all devices.</p>"""
    message_forwarding_enabled: NotRequired["bool"]
    """<p>Enables message forwarding, allowing users to forward messages from one conversation to another.</p>"""
    password_requirements: NotRequired[
        "aws_sdk_wickr.types.password_requirements.PasswordRequirements"
    ]
    """<p>The password complexity requirements that users must follow when creating or changing passwords.</p>"""
    presence_enabled: NotRequired["bool"]
    """<p>Enables presence indicators that show whether users are online, away, or offline.</p>"""
    quick_responses: NotRequired[
        "aws_sdk_wickr.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>A list of pre-defined quick response message templates that users can send with a single tap.</p>"""
    show_master_recovery_key: NotRequired["bool"]
    """<p>Users will get a master recovery key that can be used to securely sign in to their Wickr account without having access to their primary device for authentication. Available in SSO enabled network.</p>"""
    shredder: NotRequired["aws_sdk_wickr.types.shredder_settings.ShredderSettings"]
    """<p>The message shredder configuration that controls secure deletion of messages and files from devices.</p>"""
    sso_max_idle_minutes: NotRequired["int"]
    """<p>The duration for which users SSO session remains inactive before automatically logging them out for security. Available in SSO enabled network.</p>"""
    max_non_sso_session_minutes: NotRequired["int"]
    """<p>Maximum session duration in minutes for non-SSO users. Set to 0 to disable. Valid range is 60 to 525600 (1 hour to 365 days).</p>"""
    federation_mode: NotRequired["int"]
    """<p>The local federation mode controlling how users can communicate with other networks. Values: 0 (none), 1 (federated), 2 (restricted).</p>"""
    lockout_threshold: NotRequired["int"]
    """<p>The number of failed password attempts before a user account is locked out.</p>"""
    permitted_networks: NotRequired[
        "aws_sdk_wickr.types.permitted_networks_list.PermittedNetworksList"
    ]
    """<p>A list of network IDs that are permitted for local federation when federation mode is set to restricted.</p>"""
    permitted_wickr_aws_networks: NotRequired[
        "aws_sdk_wickr.types.wickr_aws_networks_list.WickrAwsNetworksList"
    ]
    """<p>A list of permitted Wickr networks for global federation, restricting communication to specific approved networks.</p>"""
    permitted_wickr_enterprise_networks: NotRequired[
        "aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list.PermittedWickrEnterpriseNetworksList"
    ]
    """<p>A list of permitted Wickr Enterprise networks for global federation, restricting communication to specific approved networks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupSettings) -> dict:
    out: dict = {}
    if "always_reauthenticate" in value:
        out["alwaysReauthenticate"] = value["always_reauthenticate"]
    if "atak_package_values" in value:
        import aws_sdk_wickr.types.security_group_string_list

        out["atakPackageValues"] = (
            aws_sdk_wickr.types.security_group_string_list.serialize_json(
                value["atak_package_values"]
            )
        )
    if "calling" in value:
        import aws_sdk_wickr.types.calling_settings

        out["calling"] = aws_sdk_wickr.types.calling_settings.serialize_json(
            value["calling"]
        )
    if "check_for_updates" in value:
        out["checkForUpdates"] = value["check_for_updates"]
    if "enable_atak" in value:
        out["enableAtak"] = value["enable_atak"]
    if "enable_crash_reports" in value:
        out["enableCrashReports"] = value["enable_crash_reports"]
    if "enable_file_download" in value:
        out["enableFileDownload"] = value["enable_file_download"]
    if "enable_guest_federation" in value:
        out["enableGuestFederation"] = value["enable_guest_federation"]
    if "enable_notification_preview" in value:
        out["enableNotificationPreview"] = value["enable_notification_preview"]
    if "enable_open_access_option" in value:
        out["enableOpenAccessOption"] = value["enable_open_access_option"]
    if "enable_restricted_global_federation" in value:
        out["enableRestrictedGlobalFederation"] = value[
            "enable_restricted_global_federation"
        ]
    if "files_enabled" in value:
        out["filesEnabled"] = value["files_enabled"]
    if "force_device_lockout" in value:
        out["forceDeviceLockout"] = value["force_device_lockout"]
    if "force_open_access" in value:
        out["forceOpenAccess"] = value["force_open_access"]
    if "force_read_receipts" in value:
        out["forceReadReceipts"] = value["force_read_receipts"]
    if "global_federation" in value:
        out["globalFederation"] = value["global_federation"]
    if "is_ato_enabled" in value:
        out["isAtoEnabled"] = value["is_ato_enabled"]
    if "is_link_preview_enabled" in value:
        out["isLinkPreviewEnabled"] = value["is_link_preview_enabled"]
    if "location_allow_maps" in value:
        out["locationAllowMaps"] = value["location_allow_maps"]
    if "location_enabled" in value:
        out["locationEnabled"] = value["location_enabled"]
    if "max_auto_download_size" in value:
        out["maxAutoDownloadSize"] = value["max_auto_download_size"]
    if "max_bor" in value:
        out["maxBor"] = value["max_bor"]
    if "max_ttl" in value:
        out["maxTtl"] = value["max_ttl"]
    if "message_forwarding_enabled" in value:
        out["messageForwardingEnabled"] = value["message_forwarding_enabled"]
    if "password_requirements" in value:
        import aws_sdk_wickr.types.password_requirements

        out["passwordRequirements"] = (
            aws_sdk_wickr.types.password_requirements.serialize_json(
                value["password_requirements"]
            )
        )
    if "presence_enabled" in value:
        out["presenceEnabled"] = value["presence_enabled"]
    if "quick_responses" in value:
        import aws_sdk_wickr.types.security_group_string_list

        out["quickResponses"] = (
            aws_sdk_wickr.types.security_group_string_list.serialize_json(
                value["quick_responses"]
            )
        )
    if "show_master_recovery_key" in value:
        out["showMasterRecoveryKey"] = value["show_master_recovery_key"]
    if "shredder" in value:
        import aws_sdk_wickr.types.shredder_settings

        out["shredder"] = aws_sdk_wickr.types.shredder_settings.serialize_json(
            value["shredder"]
        )
    if "sso_max_idle_minutes" in value:
        out["ssoMaxIdleMinutes"] = value["sso_max_idle_minutes"]
    if "max_non_sso_session_minutes" in value:
        out["maxNonSsoSessionMinutes"] = value["max_non_sso_session_minutes"]
    if "federation_mode" in value:
        out["federationMode"] = value["federation_mode"]
    if "lockout_threshold" in value:
        out["lockoutThreshold"] = value["lockout_threshold"]
    if "permitted_networks" in value:
        import aws_sdk_wickr.types.permitted_networks_list

        out["permittedNetworks"] = (
            aws_sdk_wickr.types.permitted_networks_list.serialize_json(
                value["permitted_networks"]
            )
        )
    if "permitted_wickr_aws_networks" in value:
        import aws_sdk_wickr.types.wickr_aws_networks_list

        out["permittedWickrAwsNetworks"] = (
            aws_sdk_wickr.types.wickr_aws_networks_list.serialize_json(
                value["permitted_wickr_aws_networks"]
            )
        )
    if "permitted_wickr_enterprise_networks" in value:
        import aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list

        out["permittedWickrEnterpriseNetworks"] = (
            aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list.serialize_json(
                value["permitted_wickr_enterprise_networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityGroupSettings:
    out: SecurityGroupSettings = {}  # type: ignore[typeddict-item]
    if "alwaysReauthenticate" in data:
        out["always_reauthenticate"] = data["alwaysReauthenticate"]
    if "atakPackageValues" in data:
        import aws_sdk_wickr.types.security_group_string_list

        out["atak_package_values"] = (
            aws_sdk_wickr.types.security_group_string_list.deserialize_json(
                data["atakPackageValues"]
            )
        )
    if "calling" in data:
        import aws_sdk_wickr.types.calling_settings

        out["calling"] = aws_sdk_wickr.types.calling_settings.deserialize_json(
            data["calling"]
        )
    if "checkForUpdates" in data:
        out["check_for_updates"] = data["checkForUpdates"]
    if "enableAtak" in data:
        out["enable_atak"] = data["enableAtak"]
    if "enableCrashReports" in data:
        out["enable_crash_reports"] = data["enableCrashReports"]
    if "enableFileDownload" in data:
        out["enable_file_download"] = data["enableFileDownload"]
    if "enableGuestFederation" in data:
        out["enable_guest_federation"] = data["enableGuestFederation"]
    if "enableNotificationPreview" in data:
        out["enable_notification_preview"] = data["enableNotificationPreview"]
    if "enableOpenAccessOption" in data:
        out["enable_open_access_option"] = data["enableOpenAccessOption"]
    if "enableRestrictedGlobalFederation" in data:
        out["enable_restricted_global_federation"] = data[
            "enableRestrictedGlobalFederation"
        ]
    if "filesEnabled" in data:
        out["files_enabled"] = data["filesEnabled"]
    if "forceDeviceLockout" in data:
        out["force_device_lockout"] = data["forceDeviceLockout"]
    if "forceOpenAccess" in data:
        out["force_open_access"] = data["forceOpenAccess"]
    if "forceReadReceipts" in data:
        out["force_read_receipts"] = data["forceReadReceipts"]
    if "globalFederation" in data:
        out["global_federation"] = data["globalFederation"]
    if "isAtoEnabled" in data:
        out["is_ato_enabled"] = data["isAtoEnabled"]
    if "isLinkPreviewEnabled" in data:
        out["is_link_preview_enabled"] = data["isLinkPreviewEnabled"]
    if "locationAllowMaps" in data:
        out["location_allow_maps"] = data["locationAllowMaps"]
    if "locationEnabled" in data:
        out["location_enabled"] = data["locationEnabled"]
    if "maxAutoDownloadSize" in data:
        out["max_auto_download_size"] = data["maxAutoDownloadSize"]
    if "maxBor" in data:
        out["max_bor"] = data["maxBor"]
    if "maxTtl" in data:
        out["max_ttl"] = data["maxTtl"]
    if "messageForwardingEnabled" in data:
        out["message_forwarding_enabled"] = data["messageForwardingEnabled"]
    if "passwordRequirements" in data:
        import aws_sdk_wickr.types.password_requirements

        out["password_requirements"] = (
            aws_sdk_wickr.types.password_requirements.deserialize_json(
                data["passwordRequirements"]
            )
        )
    if "presenceEnabled" in data:
        out["presence_enabled"] = data["presenceEnabled"]
    if "quickResponses" in data:
        import aws_sdk_wickr.types.security_group_string_list

        out["quick_responses"] = (
            aws_sdk_wickr.types.security_group_string_list.deserialize_json(
                data["quickResponses"]
            )
        )
    if "showMasterRecoveryKey" in data:
        out["show_master_recovery_key"] = data["showMasterRecoveryKey"]
    if "shredder" in data:
        import aws_sdk_wickr.types.shredder_settings

        out["shredder"] = aws_sdk_wickr.types.shredder_settings.deserialize_json(
            data["shredder"]
        )
    if "ssoMaxIdleMinutes" in data:
        out["sso_max_idle_minutes"] = data["ssoMaxIdleMinutes"]
    if "maxNonSsoSessionMinutes" in data:
        out["max_non_sso_session_minutes"] = data["maxNonSsoSessionMinutes"]
    if "federationMode" in data:
        out["federation_mode"] = data["federationMode"]
    if "lockoutThreshold" in data:
        out["lockout_threshold"] = data["lockoutThreshold"]
    if "permittedNetworks" in data:
        import aws_sdk_wickr.types.permitted_networks_list

        out["permitted_networks"] = (
            aws_sdk_wickr.types.permitted_networks_list.deserialize_json(
                data["permittedNetworks"]
            )
        )
    if "permittedWickrAwsNetworks" in data:
        import aws_sdk_wickr.types.wickr_aws_networks_list

        out["permitted_wickr_aws_networks"] = (
            aws_sdk_wickr.types.wickr_aws_networks_list.deserialize_json(
                data["permittedWickrAwsNetworks"]
            )
        )
    if "permittedWickrEnterpriseNetworks" in data:
        import aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list

        out["permitted_wickr_enterprise_networks"] = (
            aws_sdk_wickr.types.permitted_wickr_enterprise_networks_list.deserialize_json(
                data["permittedWickrEnterpriseNetworks"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ActiveDirectorySettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.credentials_provider
    import capo_license_manager_user_subscriptions.types.domain_network_settings
    import capo_license_manager_user_subscriptions.types.ip_v4_list
    import capo_license_manager_user_subscriptions.types.ip_v6_list


class ActiveDirectorySettings(TypedDict, closed=True):
    domain_name: NotRequired["str"]
    """<p>The domain name for the Active Directory.</p>"""
    domain_ipv4_list: NotRequired[
        "capo_license_manager_user_subscriptions.types.ip_v4_list.IpV4List"
    ]
    """<p>A list of domain IPv4 addresses that are used for the Active Directory.</p>"""
    domain_ipv6_list: NotRequired[
        "capo_license_manager_user_subscriptions.types.ip_v6_list.IpV6List"
    ]
    """<p>A list of domain IPv6 addresses that are used for the Active Directory.</p>"""
    domain_credentials_provider: NotRequired[
        "capo_license_manager_user_subscriptions.types.credentials_provider.CredentialsProvider"
    ]
    """<p>Points to the <code>CredentialsProvider</code> resource that contains information about the credential provider for user administration.</p>"""
    domain_network_settings: NotRequired[
        "capo_license_manager_user_subscriptions.types.domain_network_settings.DomainNetworkSettings"
    ]
    """<p>The <code>DomainNetworkSettings</code> resource contains an array of subnets that apply for the Active Directory.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveDirectorySettings) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "domain_ipv4_list" in value:
        import capo_license_manager_user_subscriptions.types.ip_v4_list

        out["DomainIpv4List"] = (
            capo_license_manager_user_subscriptions.types.ip_v4_list.serialize_json(
                value["domain_ipv4_list"]
            )
        )
    if "domain_ipv6_list" in value:
        import capo_license_manager_user_subscriptions.types.ip_v6_list

        out["DomainIpv6List"] = (
            capo_license_manager_user_subscriptions.types.ip_v6_list.serialize_json(
                value["domain_ipv6_list"]
            )
        )
    if "domain_credentials_provider" in value:
        import capo_license_manager_user_subscriptions.types.credentials_provider

        out["DomainCredentialsProvider"] = (
            capo_license_manager_user_subscriptions.types.credentials_provider.serialize_json(
                value["domain_credentials_provider"]
            )
        )
    if "domain_network_settings" in value:
        import capo_license_manager_user_subscriptions.types.domain_network_settings

        out["DomainNetworkSettings"] = (
            capo_license_manager_user_subscriptions.types.domain_network_settings.serialize_json(
                value["domain_network_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActiveDirectorySettings:
    out: ActiveDirectorySettings = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "DomainIpv4List" in data:
        import capo_license_manager_user_subscriptions.types.ip_v4_list

        out["domain_ipv4_list"] = (
            capo_license_manager_user_subscriptions.types.ip_v4_list.deserialize_json(
                data["DomainIpv4List"]
            )
        )
    if "DomainIpv6List" in data:
        import capo_license_manager_user_subscriptions.types.ip_v6_list

        out["domain_ipv6_list"] = (
            capo_license_manager_user_subscriptions.types.ip_v6_list.deserialize_json(
                data["DomainIpv6List"]
            )
        )
    if "DomainCredentialsProvider" in data:
        import capo_license_manager_user_subscriptions.types.credentials_provider

        out["domain_credentials_provider"] = (
            capo_license_manager_user_subscriptions.types.credentials_provider.deserialize_json(
                data["DomainCredentialsProvider"]
            )
        )
    if "DomainNetworkSettings" in data:
        import capo_license_manager_user_subscriptions.types.domain_network_settings

        out["domain_network_settings"] = (
            capo_license_manager_user_subscriptions.types.domain_network_settings.deserialize_json(
                data["DomainNetworkSettings"]
            )
        )
    return out

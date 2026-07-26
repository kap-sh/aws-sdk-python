"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroupSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.permitted_networks_list
    import capo_wickr.types.permitted_wickr_enterprise_networks_list
    import capo_wickr.types.wickr_aws_networks_list


class SecurityGroupSettingsRequest(TypedDict, closed=True):
    lockout_threshold: NotRequired["int"]
    """<p>The number of failed password attempts before a user account is locked out.</p>"""
    permitted_networks: NotRequired[
        "capo_wickr.types.permitted_networks_list.PermittedNetworksList"
    ]
    """<p>A list of network IDs that are permitted for local federation when federation mode is set to restricted.</p>"""
    enable_guest_federation: NotRequired["bool"]
    """<p>Guest users let you work with people outside your organization that only have limited access to Wickr. Only valid when federationMode is set to Global.</p>"""
    global_federation: NotRequired["bool"]
    """<p>Allow users to securely federate with all Amazon Web Services Wickr networks and Amazon Web Services Enterprise networks.</p>"""
    federation_mode: NotRequired["int"]
    """<p>The local federation mode. Values: 0 (none), 1 (federated - all networks), 2 (restricted - only permitted networks).</p>"""
    enable_restricted_global_federation: NotRequired["bool"]
    """<p>Enables restricted global federation to limit communication to specific permitted networks only. Requires globalFederation to be enabled.</p>"""
    permitted_wickr_aws_networks: NotRequired[
        "capo_wickr.types.wickr_aws_networks_list.WickrAwsNetworksList"
    ]
    """<p>A list of permitted Amazon Web Services Wickr networks for restricted global federation.</p>"""
    permitted_wickr_enterprise_networks: NotRequired[
        "capo_wickr.types.permitted_wickr_enterprise_networks_list.PermittedWickrEnterpriseNetworksList"
    ]
    """<p>A list of permitted Wickr Enterprise networks for restricted global federation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupSettingsRequest) -> dict:
    out: dict = {}
    if "lockout_threshold" in value:
        out["lockoutThreshold"] = value["lockout_threshold"]
    if "permitted_networks" in value:
        import capo_wickr.types.permitted_networks_list

        out["permittedNetworks"] = (
            capo_wickr.types.permitted_networks_list.serialize_json(
                value["permitted_networks"]
            )
        )
    if "enable_guest_federation" in value:
        out["enableGuestFederation"] = value["enable_guest_federation"]
    if "global_federation" in value:
        out["globalFederation"] = value["global_federation"]
    if "federation_mode" in value:
        out["federationMode"] = value["federation_mode"]
    if "enable_restricted_global_federation" in value:
        out["enableRestrictedGlobalFederation"] = value[
            "enable_restricted_global_federation"
        ]
    if "permitted_wickr_aws_networks" in value:
        import capo_wickr.types.wickr_aws_networks_list

        out["permittedWickrAwsNetworks"] = (
            capo_wickr.types.wickr_aws_networks_list.serialize_json(
                value["permitted_wickr_aws_networks"]
            )
        )
    if "permitted_wickr_enterprise_networks" in value:
        import capo_wickr.types.permitted_wickr_enterprise_networks_list

        out["permittedWickrEnterpriseNetworks"] = (
            capo_wickr.types.permitted_wickr_enterprise_networks_list.serialize_json(
                value["permitted_wickr_enterprise_networks"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityGroupSettingsRequest:
    out: SecurityGroupSettingsRequest = {}  # type: ignore[typeddict-item]
    if "lockoutThreshold" in data:
        out["lockout_threshold"] = data["lockoutThreshold"]
    if "permittedNetworks" in data:
        import capo_wickr.types.permitted_networks_list

        out["permitted_networks"] = (
            capo_wickr.types.permitted_networks_list.deserialize_json(
                data["permittedNetworks"]
            )
        )
    if "enableGuestFederation" in data:
        out["enable_guest_federation"] = data["enableGuestFederation"]
    if "globalFederation" in data:
        out["global_federation"] = data["globalFederation"]
    if "federationMode" in data:
        out["federation_mode"] = data["federationMode"]
    if "enableRestrictedGlobalFederation" in data:
        out["enable_restricted_global_federation"] = data[
            "enableRestrictedGlobalFederation"
        ]
    if "permittedWickrAwsNetworks" in data:
        import capo_wickr.types.wickr_aws_networks_list

        out["permitted_wickr_aws_networks"] = (
            capo_wickr.types.wickr_aws_networks_list.deserialize_json(
                data["permittedWickrAwsNetworks"]
            )
        )
    if "permittedWickrEnterpriseNetworks" in data:
        import capo_wickr.types.permitted_wickr_enterprise_networks_list

        out["permitted_wickr_enterprise_networks"] = (
            capo_wickr.types.permitted_wickr_enterprise_networks_list.deserialize_json(
                data["permittedWickrEnterpriseNetworks"]
            )
        )
    return out

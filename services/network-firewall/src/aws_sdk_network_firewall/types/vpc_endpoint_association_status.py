"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociationStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.association_sync_state
    import aws_sdk_network_firewall.types.firewall_status_value


class VpcEndpointAssociationStatus(TypedDict):
    status: "aws_sdk_network_firewall.types.firewall_status_value.FirewallStatusValue"
    """<p>The readiness of the configured firewall endpoint to handle network traffic. </p>"""
    association_sync_state: NotRequired[
        "aws_sdk_network_firewall.types.association_sync_state.AssociationSyncState"
    ]
    """<p>The list of the Availability Zone sync states for all subnets that are defined by the firewall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociationStatus) -> dict:
    out: dict = {}
    import aws_sdk_network_firewall.types.firewall_status_value

    out["Status"] = (
        aws_sdk_network_firewall.types.firewall_status_value.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "association_sync_state" in value:
        import aws_sdk_network_firewall.types.association_sync_state

        out["AssociationSyncState"] = (
            aws_sdk_network_firewall.types.association_sync_state.serialize_aws_json_1_0(
                value["association_sync_state"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointAssociationStatus:
    out: VpcEndpointAssociationStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_network_firewall.types.firewall_status_value

        out["status"] = (
            aws_sdk_network_firewall.types.firewall_status_value.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("VpcEndpointAssociationStatus.status required")
    if "AssociationSyncState" in data:
        import aws_sdk_network_firewall.types.association_sync_state

        out["association_sync_state"] = (
            aws_sdk_network_firewall.types.association_sync_state.deserialize_aws_json_1_0(
                data["AssociationSyncState"]
            )
        )
    return out

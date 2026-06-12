"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SyncState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.attachment
    import aws_sdk_network_firewall.types.sync_state_config


class SyncState(TypedDict):
    attachment: NotRequired["aws_sdk_network_firewall.types.attachment.Attachment"]
    """<p>The configuration and status for a single firewall subnet. For each configured subnet, Network Firewall creates the attachment by instantiating the firewall endpoint in the subnet so that it's ready to take traffic. </p>"""
    config: NotRequired[
        "aws_sdk_network_firewall.types.sync_state_config.SyncStateConfig"
    ]
    """<p>The configuration status of the firewall endpoint in a single VPC subnet. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncState) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_network_firewall.types.attachment

        out["Attachment"] = (
            aws_sdk_network_firewall.types.attachment.serialize_aws_json_1_0(
                value["attachment"]
            )
        )
    if "config" in value:
        import aws_sdk_network_firewall.types.sync_state_config

        out["Config"] = (
            aws_sdk_network_firewall.types.sync_state_config.serialize_aws_json_1_0(
                value["config"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncState:
    out: SyncState = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_network_firewall.types.attachment

        out["attachment"] = (
            aws_sdk_network_firewall.types.attachment.deserialize_aws_json_1_0(
                data["Attachment"]
            )
        )
    if "Config" in data:
        import aws_sdk_network_firewall.types.sync_state_config

        out["config"] = (
            aws_sdk_network_firewall.types.sync_state_config.deserialize_aws_json_1_0(
                data["Config"]
            )
        )
    return out

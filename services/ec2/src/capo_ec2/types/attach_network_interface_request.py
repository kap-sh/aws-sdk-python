"""Generated from Smithy shape ``com.amazonaws.ec2#AttachNetworkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ena_srd_specification
    import capo_ec2.types.instance_id
    import capo_ec2.types.integer
    import capo_ec2.types.network_interface_id


class AttachNetworkInterfaceRequest(TypedDict, closed=True):
    network_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network card. Some instance types support multiple network cards. The primary network interface must be assigned to network card index 0. The default is network card index 0.</p>"""
    ena_srd_specification: NotRequired[
        "capo_ec2.types.ena_srd_specification.EnaSrdSpecification"
    ]
    """<p>Configures ENA Express for the network interface that this action attaches to the instance.</p>"""
    ena_queue_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of ENA queues to be created with the instance.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the device for the network interface attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachNetworkInterfaceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_card_index" in value:
        pairs.append(
            (f"{key_prefix}NetworkCardIndex", str(value["network_card_index"]))
        )
    if "ena_srd_specification" in value:
        import capo_ec2.types.ena_srd_specification

        capo_ec2.types.ena_srd_specification.serialize_ec2_query(
            value["ena_srd_specification"], pairs, f"{key_prefix}EnaSrdSpecification"
        )
    if "ena_queue_count" in value:
        pairs.append((f"{key_prefix}EnaQueueCount", str(value["ena_queue_count"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))


def deserialize_ec2_query(el: Element) -> AttachNetworkInterfaceRequest:
    out: AttachNetworkInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_network_card_index = el.find("NetworkCardIndex")
    if child_network_card_index is not None:
        out["network_card_index"] = int(child_network_card_index.text or "")
    child_ena_srd_specification = el.find("EnaSrdSpecification")
    if child_ena_srd_specification is not None:
        import capo_ec2.types.ena_srd_specification

        out["ena_srd_specification"] = (
            capo_ec2.types.ena_srd_specification.deserialize_ec2_query(
                child_ena_srd_specification
            )
        )
    child_ena_queue_count = el.find("EnaQueueCount")
    if child_ena_queue_count is not None:
        out["ena_queue_count"] = int(child_ena_queue_count.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_device_index = el.find("deviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    return out

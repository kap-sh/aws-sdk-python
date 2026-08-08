"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.traffic_mirror_filter_id
    import capo_ec2.types.traffic_mirror_session_field_list
    import capo_ec2.types.traffic_mirror_session_id
    import capo_ec2.types.traffic_mirror_target_id


class ModifyTrafficMirrorSessionRequest(TypedDict, closed=True):
    traffic_mirror_session_id: NotRequired[
        "capo_ec2.types.traffic_mirror_session_id.TrafficMirrorSessionId"
    ]
    """<p>The ID of the Traffic Mirror session.</p>"""
    traffic_mirror_target_id: NotRequired[
        "capo_ec2.types.traffic_mirror_target_id.TrafficMirrorTargetId"
    ]
    """<p>The Traffic Mirror target. The target must be in the same VPC as the source, or have a VPC peering connection with the source.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    packet_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet.</p> <p>For sessions with Network Load Balancer (NLB) traffic mirror targets, the default <code>PacketLength</code> will be set to 8500. Valid values are 1-8500. Setting a <code>PacketLength</code> greater than 8500 will result in an error response.</p>"""
    session_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The virtual network ID of the Traffic Mirror session.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description to assign to the Traffic Mirror session.</p>"""
    remove_fields: NotRequired[
        "capo_ec2.types.traffic_mirror_session_field_list.TrafficMirrorSessionFieldList"
    ]
    """<p>The properties that you want to remove from the Traffic Mirror session.</p> <p>When you remove a property from a Traffic Mirror session, the property is set to the default.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorSessionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_session_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorSessionId",
                str(value["traffic_mirror_session_id"]),
            )
        )
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorTargetId",
                str(value["traffic_mirror_target_id"]),
            )
        )
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "packet_length" in value:
        pairs.append((f"{key_prefix}PacketLength", str(value["packet_length"])))
    if "session_number" in value:
        pairs.append((f"{key_prefix}SessionNumber", str(value["session_number"])))
    if "virtual_network_id" in value:
        pairs.append(
            (f"{key_prefix}VirtualNetworkId", str(value["virtual_network_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "remove_fields" in value:
        import capo_ec2.types.traffic_mirror_session_field_list

        capo_ec2.types.traffic_mirror_session_field_list.serialize_ec2_query(
            value["remove_fields"], pairs, f"{key_prefix}RemoveField"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTrafficMirrorSessionRequest:
    out: ModifyTrafficMirrorSessionRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_session_id = el.find("TrafficMirrorSessionId")
    if child_traffic_mirror_session_id is not None:
        out["traffic_mirror_session_id"] = str(
            child_traffic_mirror_session_id.text or ""
        )
    child_traffic_mirror_target_id = el.find("TrafficMirrorTargetId")
    if child_traffic_mirror_target_id is not None:
        out["traffic_mirror_target_id"] = str(child_traffic_mirror_target_id.text or "")
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_packet_length = el.find("PacketLength")
    if child_packet_length is not None:
        out["packet_length"] = int(child_packet_length.text or "")
    child_session_number = el.find("SessionNumber")
    if child_session_number is not None:
        out["session_number"] = int(child_session_number.text or "")
    child_virtual_network_id = el.find("VirtualNetworkId")
    if child_virtual_network_id is not None:
        out["virtual_network_id"] = int(child_virtual_network_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("RemoveField") is not None:
        import capo_ec2.types.traffic_mirror_session_field_list

        out["remove_fields"] = (
            capo_ec2.types.traffic_mirror_session_field_list.deserialize_ec2_query(
                el, "RemoveField"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

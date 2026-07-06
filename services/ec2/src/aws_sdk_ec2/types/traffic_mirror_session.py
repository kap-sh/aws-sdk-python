"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class TrafficMirrorSession(TypedDict, closed=True):
    traffic_mirror_session_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID for the Traffic Mirror session.</p>"""
    traffic_mirror_target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror target.</p>"""
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror session's network interface.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the account that owns the Traffic Mirror session.</p>"""
    packet_length: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are the bytes after the VXLAN header. To mirror a subset, set this to the length (in bytes) to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target. Do not specify this parameter when you want to mirror the entire packet</p>"""
    session_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The virtual network ID associated with the Traffic Mirror session.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror session.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorSession, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_session_id" in value:
        pairs.append(
            (
                f"{prefix}.TrafficMirrorSessionId",
                str(value["traffic_mirror_session_id"]),
            )
        )
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (f"{prefix}.TrafficMirrorTargetId", str(value["traffic_mirror_target_id"]))
        )
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (f"{prefix}.TrafficMirrorFilterId", str(value["traffic_mirror_filter_id"]))
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "packet_length" in value:
        pairs.append((f"{prefix}.PacketLength", str(value["packet_length"])))
    if "session_number" in value:
        pairs.append((f"{prefix}.SessionNumber", str(value["session_number"])))
    if "virtual_network_id" in value:
        pairs.append((f"{prefix}.VirtualNetworkId", str(value["virtual_network_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorSession:
    out: TrafficMirrorSession = {}  # type: ignore[typeddict-item]
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
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
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
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

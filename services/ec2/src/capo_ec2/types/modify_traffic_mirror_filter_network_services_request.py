"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterNetworkServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.traffic_mirror_filter_id
    import capo_ec2.types.traffic_mirror_network_service_list


class ModifyTrafficMirrorFilterNetworkServicesRequest(TypedDict, closed=True):
    traffic_mirror_filter_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    add_network_services: NotRequired[
        "capo_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service, for example Amazon DNS, that you want to mirror.</p>"""
    remove_network_services: NotRequired[
        "capo_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service, for example Amazon DNS, that you no longer want to mirror.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorFilterNetworkServicesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "add_network_services" in value:
        import capo_ec2.types.traffic_mirror_network_service_list

        capo_ec2.types.traffic_mirror_network_service_list.serialize_ec2_query(
            value["add_network_services"], pairs, f"{key_prefix}AddNetworkService"
        )
    if "remove_network_services" in value:
        import capo_ec2.types.traffic_mirror_network_service_list

        capo_ec2.types.traffic_mirror_network_service_list.serialize_ec2_query(
            value["remove_network_services"], pairs, f"{key_prefix}RemoveNetworkService"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> ModifyTrafficMirrorFilterNetworkServicesRequest:
    out: ModifyTrafficMirrorFilterNetworkServicesRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_add_network_services = el.find("AddNetworkService")
    if child_add_network_services is not None:
        import capo_ec2.types.traffic_mirror_network_service_list

        out["add_network_services"] = (
            capo_ec2.types.traffic_mirror_network_service_list.deserialize_ec2_query(
                child_add_network_services
            )
        )
    child_remove_network_services = el.find("RemoveNetworkService")
    if child_remove_network_services is not None:
        import capo_ec2.types.traffic_mirror_network_service_list

        out["remove_network_services"] = (
            capo_ec2.types.traffic_mirror_network_service_list.deserialize_ec2_query(
                child_remove_network_services
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

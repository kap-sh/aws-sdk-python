"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.traffic_mirror_filter_rule_list
    import capo_ec2.types.traffic_mirror_network_service_list


class TrafficMirrorFilter(TypedDict, closed=True):
    traffic_mirror_filter_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    ingress_filter_rules: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_rule_list.TrafficMirrorFilterRuleList"
    ]
    """<p>Information about the ingress rules that are associated with the Traffic Mirror filter.</p>"""
    egress_filter_rules: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_rule_list.TrafficMirrorFilterRuleList"
    ]
    """<p>Information about the egress rules that are associated with the Traffic Mirror filter.</p>"""
    network_services: NotRequired[
        "capo_ec2.types.traffic_mirror_network_service_list.TrafficMirrorNetworkServiceList"
    ]
    """<p>The network service traffic that is associated with the Traffic Mirror filter.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror filter.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the Traffic Mirror filter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "ingress_filter_rules" in value:
        import capo_ec2.types.traffic_mirror_filter_rule_list

        capo_ec2.types.traffic_mirror_filter_rule_list.serialize_ec2_query(
            value["ingress_filter_rules"], pairs, f"{key_prefix}IngressFilterRuleSet"
        )
    if "egress_filter_rules" in value:
        import capo_ec2.types.traffic_mirror_filter_rule_list

        capo_ec2.types.traffic_mirror_filter_rule_list.serialize_ec2_query(
            value["egress_filter_rules"], pairs, f"{key_prefix}EgressFilterRuleSet"
        )
    if "network_services" in value:
        import capo_ec2.types.traffic_mirror_network_service_list

        capo_ec2.types.traffic_mirror_network_service_list.serialize_ec2_query(
            value["network_services"], pairs, f"{key_prefix}NetworkServiceSet"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorFilter:
    out: TrafficMirrorFilter = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    if el.find("IngressFilterRuleSet") is not None:
        import capo_ec2.types.traffic_mirror_filter_rule_list

        out["ingress_filter_rules"] = (
            capo_ec2.types.traffic_mirror_filter_rule_list.deserialize_ec2_query(
                el, "IngressFilterRuleSet"
            )
        )
    if el.find("EgressFilterRuleSet") is not None:
        import capo_ec2.types.traffic_mirror_filter_rule_list

        out["egress_filter_rules"] = (
            capo_ec2.types.traffic_mirror_filter_rule_list.deserialize_ec2_query(
                el, "EgressFilterRuleSet"
            )
        )
    if el.find("NetworkServiceSet") is not None:
        import capo_ec2.types.traffic_mirror_network_service_list

        out["network_services"] = (
            capo_ec2.types.traffic_mirror_network_service_list.deserialize_ec2_query(
                el, "NetworkServiceSet"
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

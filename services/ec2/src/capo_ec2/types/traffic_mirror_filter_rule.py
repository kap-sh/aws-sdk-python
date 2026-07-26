"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorFilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.traffic_direction
    import capo_ec2.types.traffic_mirror_port_range
    import capo_ec2.types.traffic_mirror_rule_action


class TrafficMirrorFilterRule(TypedDict, closed=True):
    traffic_mirror_filter_rule_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    traffic_mirror_filter_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter that the rule is associated with.</p>"""
    traffic_direction: NotRequired["capo_ec2.types.traffic_direction.TrafficDirection"]
    """<p>The traffic direction assigned to the Traffic Mirror rule.</p>"""
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number of the Traffic Mirror rule.</p>"""
    rule_action: NotRequired[
        "capo_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action assigned to the Traffic Mirror rule.</p>"""
    protocol: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The protocol assigned to the Traffic Mirror rule.</p>"""
    destination_port_range: NotRequired[
        "capo_ec2.types.traffic_mirror_port_range.TrafficMirrorPortRange"
    ]
    """<p>The destination port range assigned to the Traffic Mirror rule.</p>"""
    source_port_range: NotRequired[
        "capo_ec2.types.traffic_mirror_port_range.TrafficMirrorPortRange"
    ]
    """<p>The source port range assigned to the Traffic Mirror rule.</p>"""
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block assigned to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The source CIDR block assigned to the Traffic Mirror rule.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror rule.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Tags on Traffic Mirroring filter rules.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorFilterRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_filter_rule_id" in value:
        pairs.append(
            (
                f"{prefix}.TrafficMirrorFilterRuleId",
                str(value["traffic_mirror_filter_rule_id"]),
            )
        )
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (f"{prefix}.TrafficMirrorFilterId", str(value["traffic_mirror_filter_id"]))
        )
    if "traffic_direction" in value:
        import capo_ec2.types.traffic_direction

        capo_ec2.types.traffic_direction.serialize_ec2_query(
            value["traffic_direction"], pairs, f"{prefix}.TrafficDirection"
        )
    if "rule_number" in value:
        pairs.append((f"{prefix}.RuleNumber", str(value["rule_number"])))
    if "rule_action" in value:
        import capo_ec2.types.traffic_mirror_rule_action

        capo_ec2.types.traffic_mirror_rule_action.serialize_ec2_query(
            value["rule_action"], pairs, f"{prefix}.RuleAction"
        )
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "destination_port_range" in value:
        import capo_ec2.types.traffic_mirror_port_range

        capo_ec2.types.traffic_mirror_port_range.serialize_ec2_query(
            value["destination_port_range"], pairs, f"{prefix}.DestinationPortRange"
        )
    if "source_port_range" in value:
        import capo_ec2.types.traffic_mirror_port_range

        capo_ec2.types.traffic_mirror_port_range.serialize_ec2_query(
            value["source_port_range"], pairs, f"{prefix}.SourcePortRange"
        )
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "source_cidr_block" in value:
        pairs.append((f"{prefix}.SourceCidrBlock", str(value["source_cidr_block"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> TrafficMirrorFilterRule:
    out: TrafficMirrorFilterRule = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule_id = el.find("TrafficMirrorFilterRuleId")
    if child_traffic_mirror_filter_rule_id is not None:
        out["traffic_mirror_filter_rule_id"] = str(
            child_traffic_mirror_filter_rule_id.text or ""
        )
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_traffic_direction = el.find("TrafficDirection")
    if child_traffic_direction is not None:
        import capo_ec2.types.traffic_direction

        out["traffic_direction"] = (
            capo_ec2.types.traffic_direction.deserialize_ec2_query(
                child_traffic_direction
            )
        )
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        import capo_ec2.types.traffic_mirror_rule_action

        out["rule_action"] = (
            capo_ec2.types.traffic_mirror_rule_action.deserialize_ec2_query(
                child_rule_action
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = int(child_protocol.text or "")
    child_destination_port_range = el.find("DestinationPortRange")
    if child_destination_port_range is not None:
        import capo_ec2.types.traffic_mirror_port_range

        out["destination_port_range"] = (
            capo_ec2.types.traffic_mirror_port_range.deserialize_ec2_query(
                child_destination_port_range
            )
        )
    child_source_port_range = el.find("SourcePortRange")
    if child_source_port_range is not None:
        import capo_ec2.types.traffic_mirror_port_range

        out["source_port_range"] = (
            capo_ec2.types.traffic_mirror_port_range.deserialize_ec2_query(
                child_source_port_range
            )
        )
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_source_cidr_block = el.find("SourceCidrBlock")
    if child_source_cidr_block is not None:
        out["source_cidr_block"] = str(child_source_cidr_block.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out

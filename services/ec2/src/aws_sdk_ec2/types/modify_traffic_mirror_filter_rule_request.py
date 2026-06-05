"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.traffic_direction
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list
    import aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver
    import aws_sdk_ec2.types.traffic_mirror_port_range_request
    import aws_sdk_ec2.types.traffic_mirror_rule_action


class ModifyTrafficMirrorFilterRuleRequest(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_id_with_resolver.TrafficMirrorFilterRuleIdWithResolver"
    ]
    """<p>The ID of the Traffic Mirror rule.</p>"""
    traffic_direction: NotRequired[
        "aws_sdk_ec2.types.traffic_direction.TrafficDirection"
    ]
    """<p>The type of traffic to assign to the rule.</p>"""
    rule_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.</p>"""
    rule_action: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action to assign to the rule.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The destination ports that are associated with the Traffic Mirror rule.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The port range to assign to the Traffic Mirror rule.</p>"""
    protocol: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The protocol, for example TCP, to assign to the Traffic Mirror rule.</p>"""
    destination_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination CIDR block to assign to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source CIDR block to assign to the Traffic Mirror rule.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description to assign to the Traffic Mirror rule.</p>"""
    remove_fields: NotRequired[
        "aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list.TrafficMirrorFilterRuleFieldList"
    ]
    """<p>The properties that you want to remove from the Traffic Mirror filter rule.</p> <p>When you remove a property from a Traffic Mirror filter rule, the property is set to the default.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorFilterRuleRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter_rule_id" in value:
        pairs.append(
            (
                f"{prefix}.TrafficMirrorFilterRuleId",
                str(value["traffic_mirror_filter_rule_id"]),
            )
        )
    if "traffic_direction" in value:
        import aws_sdk_ec2.types.traffic_direction

        aws_sdk_ec2.types.traffic_direction.serialize_ec2_query(
            value["traffic_direction"], pairs, f"{prefix}.TrafficDirection"
        )
    if "rule_number" in value:
        pairs.append((f"{prefix}.RuleNumber", str(value["rule_number"])))
    if "rule_action" in value:
        import aws_sdk_ec2.types.traffic_mirror_rule_action

        aws_sdk_ec2.types.traffic_mirror_rule_action.serialize_ec2_query(
            value["rule_action"], pairs, f"{prefix}.RuleAction"
        )
    if "destination_port_range" in value:
        import aws_sdk_ec2.types.traffic_mirror_port_range_request

        aws_sdk_ec2.types.traffic_mirror_port_range_request.serialize_ec2_query(
            value["destination_port_range"], pairs, f"{prefix}.DestinationPortRange"
        )
    if "source_port_range" in value:
        import aws_sdk_ec2.types.traffic_mirror_port_range_request

        aws_sdk_ec2.types.traffic_mirror_port_range_request.serialize_ec2_query(
            value["source_port_range"], pairs, f"{prefix}.SourcePortRange"
        )
    if "protocol" in value:
        pairs.append((f"{prefix}.Protocol", str(value["protocol"])))
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{prefix}.DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "source_cidr_block" in value:
        pairs.append((f"{prefix}.SourceCidrBlock", str(value["source_cidr_block"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "remove_fields" in value:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list

        aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list.serialize_ec2_query(
            value["remove_fields"], pairs, f"{prefix}.RemoveFields"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTrafficMirrorFilterRuleRequest:
    out: ModifyTrafficMirrorFilterRuleRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule_id = el.find("TrafficMirrorFilterRuleId")
    if child_traffic_mirror_filter_rule_id is not None:
        out["traffic_mirror_filter_rule_id"] = str(
            child_traffic_mirror_filter_rule_id.text or ""
        )
    child_traffic_direction = el.find("TrafficDirection")
    if child_traffic_direction is not None:
        import aws_sdk_ec2.types.traffic_direction

        out["traffic_direction"] = (
            aws_sdk_ec2.types.traffic_direction.deserialize_ec2_query(
                child_traffic_direction
            )
        )
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        import aws_sdk_ec2.types.traffic_mirror_rule_action

        out["rule_action"] = (
            aws_sdk_ec2.types.traffic_mirror_rule_action.deserialize_ec2_query(
                child_rule_action
            )
        )
    child_destination_port_range = el.find("DestinationPortRange")
    if child_destination_port_range is not None:
        import aws_sdk_ec2.types.traffic_mirror_port_range_request

        out["destination_port_range"] = (
            aws_sdk_ec2.types.traffic_mirror_port_range_request.deserialize_ec2_query(
                child_destination_port_range
            )
        )
    child_source_port_range = el.find("SourcePortRange")
    if child_source_port_range is not None:
        import aws_sdk_ec2.types.traffic_mirror_port_range_request

        out["source_port_range"] = (
            aws_sdk_ec2.types.traffic_mirror_port_range_request.deserialize_ec2_query(
                child_source_port_range
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = int(child_protocol.text or "")
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_source_cidr_block = el.find("SourceCidrBlock")
    if child_source_cidr_block is not None:
        out["source_cidr_block"] = str(child_source_cidr_block.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    if el.find("RemoveFields") is not None:
        import aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list

        out["remove_fields"] = (
            aws_sdk_ec2.types.traffic_mirror_filter_rule_field_list.deserialize_ec2_query(
                el, "RemoveFields"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out

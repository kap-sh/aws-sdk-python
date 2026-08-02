"""Generated from Smithy shape ``com.amazonaws.ec2#PlacementGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.operator_response
    import capo_ec2.types.placement_group_id
    import capo_ec2.types.placement_group_state
    import capo_ec2.types.placement_strategy
    import capo_ec2.types.spread_level
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class PlacementGroup(TypedDict, closed=True):
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the placement group.</p>"""
    state: NotRequired["capo_ec2.types.placement_group_state.PlacementGroupState"]
    """<p>The state of the placement group.</p>"""
    strategy: NotRequired["capo_ec2.types.placement_strategy.PlacementStrategy"]
    """<p>The placement strategy.</p>"""
    partition_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of partitions. Valid only if <b>strategy</b> is set to <code>partition</code>.</p>"""
    group_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the placement group.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the placement group.</p>"""
    group_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the placement group.</p>"""
    spread_level: NotRequired["capo_ec2.types.spread_level.SpreadLevel"]
    """<p>The spread level for the placement group. <i>Only</i> Outpost placement groups can be spread across hosts.</p>"""
    linked_group_id: NotRequired["capo_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>Reserved for future use.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the Placement Group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PlacementGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "state" in value:
        import capo_ec2.types.placement_group_state

        capo_ec2.types.placement_group_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "strategy" in value:
        import capo_ec2.types.placement_strategy

        capo_ec2.types.placement_strategy.serialize_ec2_query(
            value["strategy"], pairs, f"{key_prefix}Strategy"
        )
    if "partition_count" in value:
        pairs.append((f"{key_prefix}PartitionCount", str(value["partition_count"])))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "group_arn" in value:
        pairs.append((f"{key_prefix}GroupArn", str(value["group_arn"])))
    if "spread_level" in value:
        import capo_ec2.types.spread_level

        capo_ec2.types.spread_level.serialize_ec2_query(
            value["spread_level"], pairs, f"{key_prefix}SpreadLevel"
        )
    if "linked_group_id" in value:
        pairs.append((f"{key_prefix}LinkedGroupId", str(value["linked_group_id"])))
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )


def deserialize_ec2_query(el: Element) -> PlacementGroup:
    out: PlacementGroup = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.placement_group_state

        out["state"] = capo_ec2.types.placement_group_state.deserialize_ec2_query(
            child_state
        )
    child_strategy = el.find("Strategy")
    if child_strategy is not None:
        import capo_ec2.types.placement_strategy

        out["strategy"] = capo_ec2.types.placement_strategy.deserialize_ec2_query(
            child_strategy
        )
    child_partition_count = el.find("PartitionCount")
    if child_partition_count is not None:
        out["partition_count"] = int(child_partition_count.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_group_arn = el.find("GroupArn")
    if child_group_arn is not None:
        out["group_arn"] = str(child_group_arn.text or "")
    child_spread_level = el.find("SpreadLevel")
    if child_spread_level is not None:
        import capo_ec2.types.spread_level

        out["spread_level"] = capo_ec2.types.spread_level.deserialize_ec2_query(
            child_spread_level
        )
    child_linked_group_id = el.find("LinkedGroupId")
    if child_linked_group_id is not None:
        out["linked_group_id"] = str(child_linked_group_id.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out

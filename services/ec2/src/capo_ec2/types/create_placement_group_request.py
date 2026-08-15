"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePlacementGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.operator_request
    import capo_ec2.types.placement_group_id
    import capo_ec2.types.placement_strategy
    import capo_ec2.types.spread_level
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreatePlacementGroupRequest(TypedDict, closed=True):
    partition_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of partitions. Valid only when <b>Strategy</b> is set to <code>partition</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new placement group.</p>"""
    spread_level: NotRequired["capo_ec2.types.spread_level.SpreadLevel"]
    """<p>Determines how placement groups spread instances. </p> <ul> <li> <p>Host – You can use <code>host</code> only with Outpost placement groups.</p> </li> <li> <p>Rack – No usage restrictions.</p> </li> </ul>"""
    linked_group_id: NotRequired["capo_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>Reserved for future use.</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    parent_group_id: NotRequired["capo_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The ID of a parent placement group. Valid only when <b>Strategy</b> is set to <code>cluster</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>A name for the placement group. Must be unique within the scope of your account for the Region.</p> <p>Constraints: Up to 255 ASCII characters</p>"""
    strategy: NotRequired["capo_ec2.types.placement_strategy.PlacementStrategy"]
    """<p>The placement strategy.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreatePlacementGroupRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "partition_count" in value:
        pairs.append((f"{key_prefix}PartitionCount", str(value["partition_count"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "spread_level" in value:
        import capo_ec2.types.spread_level

        capo_ec2.types.spread_level.serialize_ec2_query(
            value["spread_level"], pairs, f"{key_prefix}SpreadLevel"
        )
    if "linked_group_id" in value:
        pairs.append((f"{key_prefix}LinkedGroupId", str(value["linked_group_id"])))
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "parent_group_id" in value:
        pairs.append((f"{key_prefix}ParentGroupId", str(value["parent_group_id"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "strategy" in value:
        import capo_ec2.types.placement_strategy

        capo_ec2.types.placement_strategy.serialize_ec2_query(
            value["strategy"], pairs, f"{key_prefix}Strategy"
        )


def deserialize_ec2_query(el: Element) -> CreatePlacementGroupRequest:
    out: CreatePlacementGroupRequest = {}  # type: ignore[typeddict-item]
    child_partition_count = el.find("PartitionCount")
    if child_partition_count is not None:
        out["partition_count"] = int(child_partition_count.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
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
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_parent_group_id = el.find("ParentGroupId")
    if child_parent_group_id is not None:
        out["parent_group_id"] = str(child_parent_group_id.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_strategy = el.find("strategy")
    if child_strategy is not None:
        import capo_ec2.types.placement_strategy

        out["strategy"] = capo_ec2.types.placement_strategy.deserialize_ec2_query(
            child_strategy
        )
    return out

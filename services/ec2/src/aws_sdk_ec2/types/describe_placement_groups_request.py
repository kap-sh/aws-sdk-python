"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePlacementGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.placement_group_id_string_list
    import aws_sdk_ec2.types.placement_group_string_list


class DescribePlacementGroupsRequest(TypedDict, closed=True):
    group_ids: NotRequired[
        "aws_sdk_ec2.types.placement_group_id_string_list.PlacementGroupIdStringList"
    ]
    """<p>The IDs of the placement groups.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_names: NotRequired[
        "aws_sdk_ec2.types.placement_group_string_list.PlacementGroupStringList"
    ]
    """<p>The names of the placement groups.</p> <p>Constraints:</p> <ul> <li> <p>You can specify a name only if the placement group is owned by your account.</p> </li> <li> <p>If a placement group is <i>shared</i> with your account, specifying the name results in an error. You must use the <code>GroupId</code> parameter instead.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>group-name</code> - The name of the placement group.</p> </li> <li> <p> <code>group-arn</code> - The Amazon Resource Name (ARN) of the placement group.</p> </li> <li> <p> <code>spread-level</code> - The spread level for the placement group (<code>host</code> | <code>rack</code>). </p> </li> <li> <p> <code>state</code> - The state of the placement group (<code>pending</code> | <code>available</code> | <code>deleting</code> | <code>deleted</code>).</p> </li> <li> <p> <code>strategy</code> - The strategy of the placement group (<code>cluster</code> | <code>spread</code> | <code>partition</code>).</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribePlacementGroupsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_ids" in value:
        import aws_sdk_ec2.types.placement_group_id_string_list

        aws_sdk_ec2.types.placement_group_id_string_list.serialize_ec2_query(
            value["group_ids"], pairs, f"{prefix}.GroupIds"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "group_names" in value:
        import aws_sdk_ec2.types.placement_group_string_list

        aws_sdk_ec2.types.placement_group_string_list.serialize_ec2_query(
            value["group_names"], pairs, f"{prefix}.GroupName"
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_ec2_query(el: Element) -> DescribePlacementGroupsRequest:
    out: DescribePlacementGroupsRequest = {}  # type: ignore[typeddict-item]
    if el.find("GroupIds") is not None:
        import aws_sdk_ec2.types.placement_group_id_string_list

        out["group_ids"] = (
            aws_sdk_ec2.types.placement_group_id_string_list.deserialize_ec2_query(
                el, "GroupIds"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("GroupName") is not None:
        import aws_sdk_ec2.types.placement_group_string_list

        out["group_names"] = (
            aws_sdk_ec2.types.placement_group_string_list.deserialize_ec2_query(
                el, "GroupName"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTrunkInterfaceAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_trunk_interface_associations_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string
    import capo_ec2.types.trunk_interface_association_id_list


class DescribeTrunkInterfaceAssociationsRequest(TypedDict, closed=True):
    association_ids: NotRequired[
        "capo_ec2.types.trunk_interface_association_id_list.TrunkInterfaceAssociationIdList"
    ]
    """<p>The IDs of the associations.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>gre-key</code> - The ID of a trunk interface association.</p> </li> <li> <p> <code>interface-protocol</code> - The interface protocol. Valid values are <code>VLAN</code> and <code>GRE</code>.</p> </li> </ul>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_trunk_interface_associations_max_results.DescribeTrunkInterfaceAssociationsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTrunkInterfaceAssociationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "association_ids" in value:
        import capo_ec2.types.trunk_interface_association_id_list

        capo_ec2.types.trunk_interface_association_id_list.serialize_ec2_query(
            value["association_ids"], pairs, f"{key_prefix}AssociationId"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))


def deserialize_ec2_query(el: Element) -> DescribeTrunkInterfaceAssociationsRequest:
    out: DescribeTrunkInterfaceAssociationsRequest = {}  # type: ignore[typeddict-item]
    child_association_ids = el.find("AssociationId")
    if child_association_ids is not None:
        import capo_ec2.types.trunk_interface_association_id_list

        out["association_ids"] = (
            capo_ec2.types.trunk_interface_association_id_list.deserialize_ec2_query(
                child_association_ids
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    return out

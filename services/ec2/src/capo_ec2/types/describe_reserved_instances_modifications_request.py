"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeReservedInstancesModificationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.filter_list
    import capo_ec2.types.reserved_instances_modification_id_string_list
    import capo_ec2.types.string


class DescribeReservedInstancesModificationsRequest(TypedDict, closed=True):
    reserved_instances_modification_ids: NotRequired[
        "capo_ec2.types.reserved_instances_modification_id_string_list.ReservedInstancesModificationIdStringList"
    ]
    """<p>IDs for the submitted modification request.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to retrieve the next page of results.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>client-token</code> - The idempotency token for the modification request.</p> </li> <li> <p> <code>create-date</code> - The time when the modification request was created.</p> </li> <li> <p> <code>effective-date</code> - The time when the modification becomes effective.</p> </li> <li> <p> <code>modification-result.reserved-instances-id</code> - The ID for the Reserved Instances created as part of the modification request. This ID is only available when the status of the modification is <code>fulfilled</code>.</p> </li> <li> <p> <code>modification-result.target-configuration.availability-zone</code> - The Availability Zone for the new Reserved Instances.</p> </li> <li> <p> <code>modification-result.target-configuration.availability-zone-id</code> - The ID of the Availability Zone for the new Reserved Instances.</p> </li> <li> <p> <code>modification-result.target-configuration.instance-count </code> - The number of new Reserved Instances.</p> </li> <li> <p> <code>modification-result.target-configuration.instance-type</code> - The instance type of the new Reserved Instances.</p> </li> <li> <p> <code>reserved-instances-id</code> - The ID of the Reserved Instances modified.</p> </li> <li> <p> <code>reserved-instances-modification-id</code> - The ID of the modification request.</p> </li> <li> <p> <code>status</code> - The status of the Reserved Instances modification request (<code>processing</code> | <code>fulfilled</code> | <code>failed</code>).</p> </li> <li> <p> <code>status-message</code> - The reason for the status.</p> </li> <li> <p> <code>update-date</code> - The time when the modification request was last updated.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeReservedInstancesModificationsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_modification_ids" in value:
        import capo_ec2.types.reserved_instances_modification_id_string_list

        capo_ec2.types.reserved_instances_modification_id_string_list.serialize_ec2_query(
            value["reserved_instances_modification_ids"],
            pairs,
            f"{key_prefix}ReservedInstancesModificationId",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeReservedInstancesModificationsRequest:
    out: DescribeReservedInstancesModificationsRequest = {}  # type: ignore[typeddict-item]
    if el.find("ReservedInstancesModificationId") is not None:
        import capo_ec2.types.reserved_instances_modification_id_string_list

        out["reserved_instances_modification_ids"] = (
            capo_ec2.types.reserved_instances_modification_id_string_list.deserialize_ec2_query(
                el, "ReservedInstancesModificationId"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("Filter") is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(el, "Filter")
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseReservedInstancesOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.reserved_instance_limit_price
    import capo_ec2.types.reserved_instances_offering_id


class PurchaseReservedInstancesOfferingRequest(TypedDict, closed=True):
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of Reserved Instances to purchase.</p>"""
    reserved_instances_offering_id: NotRequired[
        "capo_ec2.types.reserved_instances_offering_id.ReservedInstancesOfferingId"
    ]
    """<p>The ID of the Reserved Instance offering to purchase.</p>"""
    purchase_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time at which to purchase the Reserved Instance, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    limit_price: NotRequired[
        "capo_ec2.types.reserved_instance_limit_price.ReservedInstanceLimitPrice"
    ]
    """<p>Specified for Reserved Instance Marketplace offerings to limit the total order and ensure that the Reserved Instances are not purchased at unexpected prices.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PurchaseReservedInstancesOfferingRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "reserved_instances_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedInstancesOfferingId",
                str(value["reserved_instances_offering_id"]),
            )
        )
    if "purchase_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["purchase_time"], pairs, f"{key_prefix}PurchaseTime"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "limit_price" in value:
        import capo_ec2.types.reserved_instance_limit_price

        capo_ec2.types.reserved_instance_limit_price.serialize_ec2_query(
            value["limit_price"], pairs, f"{key_prefix}LimitPrice"
        )


def deserialize_ec2_query(el: Element) -> PurchaseReservedInstancesOfferingRequest:
    out: PurchaseReservedInstancesOfferingRequest = {}  # type: ignore[typeddict-item]
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_reserved_instances_offering_id = el.find("ReservedInstancesOfferingId")
    if child_reserved_instances_offering_id is not None:
        out["reserved_instances_offering_id"] = str(
            child_reserved_instances_offering_id.text or ""
        )
    child_purchase_time = el.find("PurchaseTime")
    if child_purchase_time is not None:
        import capo_ec2.types.date_time

        out["purchase_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_purchase_time
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_limit_price = el.find("limitPrice")
    if child_limit_price is not None:
        import capo_ec2.types.reserved_instance_limit_price

        out["limit_price"] = (
            capo_ec2.types.reserved_instance_limit_price.deserialize_ec2_query(
                child_limit_price
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#ReservedNodeOffering``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.double
    import aws_sdk_redshift.types.integer
    import aws_sdk_redshift.types.recurring_charge_list
    import aws_sdk_redshift.types.reserved_node_offering_type
    import aws_sdk_redshift.types.string


class ReservedNodeOffering(TypedDict):
    reserved_node_offering_id: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The offering identifier.</p>"""
    node_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The node type offered by the reserved node offering.</p>"""
    duration: NotRequired["aws_sdk_redshift.types.integer.Integer"]
    """<p>The duration, in seconds, for which the offering will reserve the node.</p>"""
    fixed_price: NotRequired["aws_sdk_redshift.types.double.Double"]
    """<p>The upfront fixed charge you will pay to purchase the specific reserved node offering.</p>"""
    usage_price: NotRequired["aws_sdk_redshift.types.double.Double"]
    """<p>The rate you are charged for each hour the cluster that is using the offering is running.</p>"""
    currency_code: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The currency code for the compute nodes offering.</p>"""
    offering_type: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The anticipated utilization of the reserved node, as defined in the reserved node offering.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_redshift.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The charge to your account regardless of whether you are creating any clusters using the node offering. Recurring charges are only in effect for heavy-utilization reserved nodes.</p>"""
    reserved_node_offering_type: NotRequired[
        "aws_sdk_redshift.types.reserved_node_offering_type.ReservedNodeOfferingType"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedNodeOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedNodeOfferingId",
                str(value["reserved_node_offering_id"]),
            )
        )
    if "node_type" in value:
        pairs.append((f"{prefix}.NodeType", str(value["node_type"])))
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "fixed_price" in value:
        pairs.append((f"{prefix}.FixedPrice", str(value["fixed_price"])))
    if "usage_price" in value:
        pairs.append((f"{prefix}.UsagePrice", str(value["usage_price"])))
    if "currency_code" in value:
        pairs.append((f"{prefix}.CurrencyCode", str(value["currency_code"])))
    if "offering_type" in value:
        pairs.append((f"{prefix}.OfferingType", str(value["offering_type"])))
    if "recurring_charges" in value:
        import aws_sdk_redshift.types.recurring_charge_list

        aws_sdk_redshift.types.recurring_charge_list.serialize_query(
            value["recurring_charges"], pairs, f"{prefix}.RecurringCharges"
        )
    if "reserved_node_offering_type" in value:
        import aws_sdk_redshift.types.reserved_node_offering_type

        aws_sdk_redshift.types.reserved_node_offering_type.serialize_query(
            value["reserved_node_offering_type"],
            pairs,
            f"{prefix}.ReservedNodeOfferingType",
        )


def deserialize_query(el: Element) -> ReservedNodeOffering:
    out: ReservedNodeOffering = {}  # type: ignore[typeddict-item]
    child_reserved_node_offering_id = el.find("ReservedNodeOfferingId")
    if child_reserved_node_offering_id is not None:
        out["reserved_node_offering_id"] = str(
            child_reserved_node_offering_id.text or ""
        )
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_fixed_price = el.find("FixedPrice")
    if child_fixed_price is not None:
        out["fixed_price"] = float(child_fixed_price.text or "")
    child_usage_price = el.find("UsagePrice")
    if child_usage_price is not None:
        out["usage_price"] = float(child_usage_price.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        out["currency_code"] = str(child_currency_code.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_recurring_charges = el.find("RecurringCharges")
    if child_recurring_charges is not None:
        import aws_sdk_redshift.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_redshift.types.recurring_charge_list.deserialize_query(
                child_recurring_charges
            )
        )
    child_reserved_node_offering_type = el.find("ReservedNodeOfferingType")
    if child_reserved_node_offering_type is not None:
        import aws_sdk_redshift.types.reserved_node_offering_type

        out["reserved_node_offering_type"] = (
            aws_sdk_redshift.types.reserved_node_offering_type.deserialize_query(
                child_reserved_node_offering_type
            )
        )
    return out

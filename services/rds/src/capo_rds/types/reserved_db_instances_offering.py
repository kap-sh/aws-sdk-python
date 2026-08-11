"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstancesOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.double
    import capo_rds.types.integer
    import capo_rds.types.recurring_charge_list
    import capo_rds.types.string


class ReservedDBInstancesOffering(TypedDict, closed=True):
    reserved_db_instances_offering_id: NotRequired["capo_rds.types.string.String"]
    """<p>The offering identifier.</p>"""
    db_instance_class: NotRequired["capo_rds.types.string.String"]
    """<p>The DB instance class for the reserved DB instance.</p>"""
    duration: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The duration of the offering in seconds.</p>"""
    fixed_price: NotRequired["capo_rds.types.double.Double"]
    """<p>The fixed price charged for this offering.</p>"""
    usage_price: NotRequired["capo_rds.types.double.Double"]
    """<p>The hourly price charged for this offering.</p>"""
    currency_code: NotRequired["capo_rds.types.string.String"]
    """<p>The currency code for the reserved DB instance offering.</p>"""
    product_description: NotRequired["capo_rds.types.string.String"]
    """<p>The database engine used by the offering.</p>"""
    offering_type: NotRequired["capo_rds.types.string.String"]
    """<p>The offering type.</p>"""
    multi_az: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the offering applies to Multi-AZ deployments.</p>"""
    recurring_charges: NotRequired[
        "capo_rds.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstancesOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_db_instances_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedDBInstancesOfferingId",
                str(value["reserved_db_instances_offering_id"]),
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{key_prefix}DBInstanceClass", str(value["db_instance_class"])))
    if "duration" in value:
        pairs.append((f"{key_prefix}Duration", str(value["duration"])))
    if "fixed_price" in value:
        pairs.append(
            (
                f"{key_prefix}FixedPrice",
                (
                    "NaN"
                    if value["fixed_price"] != value["fixed_price"]
                    else "Infinity"
                    if value["fixed_price"] == float("inf")
                    else "-Infinity"
                    if value["fixed_price"] == float("-inf")
                    else str(value["fixed_price"])
                ),
            )
        )
    if "usage_price" in value:
        pairs.append(
            (
                f"{key_prefix}UsagePrice",
                (
                    "NaN"
                    if value["usage_price"] != value["usage_price"]
                    else "Infinity"
                    if value["usage_price"] == float("inf")
                    else "-Infinity"
                    if value["usage_price"] == float("-inf")
                    else str(value["usage_price"])
                ),
            )
        )
    if "currency_code" in value:
        pairs.append((f"{key_prefix}CurrencyCode", str(value["currency_code"])))
    if "product_description" in value:
        pairs.append(
            (f"{key_prefix}ProductDescription", str(value["product_description"]))
        )
    if "offering_type" in value:
        pairs.append((f"{key_prefix}OfferingType", str(value["offering_type"])))
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "recurring_charges" in value:
        import capo_rds.types.recurring_charge_list

        capo_rds.types.recurring_charge_list.serialize_query(
            value["recurring_charges"], pairs, f"{key_prefix}RecurringCharges"
        )


def deserialize_query(el: Element) -> ReservedDBInstancesOffering:
    out: ReservedDBInstancesOffering = {}  # type: ignore[typeddict-item]
    child_reserved_db_instances_offering_id = el.find("ReservedDBInstancesOfferingId")
    if child_reserved_db_instances_offering_id is not None:
        out["reserved_db_instances_offering_id"] = str(
            child_reserved_db_instances_offering_id.text or ""
        )
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
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
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        out["product_description"] = str(child_product_description.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_recurring_charges = el.find("RecurringCharges")
    if child_recurring_charges is not None:
        import capo_rds.types.recurring_charge_list

        out["recurring_charges"] = (
            capo_rds.types.recurring_charge_list.deserialize_query(
                child_recurring_charges
            )
        )
    return out

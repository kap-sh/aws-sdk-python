"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.double
    import aws_sdk_rds.types.integer
    import aws_sdk_rds.types.recurring_charge_list
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.t_stamp


class ReservedDBInstance(TypedDict, closed=True):
    reserved_db_instance_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The unique identifier for the reservation.</p>"""
    reserved_db_instances_offering_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The offering identifier.</p>"""
    db_instance_class: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The DB instance class for the reserved DB instance.</p>"""
    start_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time the reservation started.</p>"""
    duration: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>The duration of the reservation in seconds.</p>"""
    fixed_price: NotRequired["aws_sdk_rds.types.double.Double"]
    """<p>The fixed price charged for this reserved DB instance.</p>"""
    usage_price: NotRequired["aws_sdk_rds.types.double.Double"]
    """<p>The hourly price charged for this reserved DB instance.</p>"""
    currency_code: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The currency code for the reserved DB instance.</p>"""
    db_instance_count: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>The number of reserved DB instances.</p>"""
    product_description: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The description of the reserved DB instance.</p>"""
    offering_type: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The offering type of this reserved DB instance.</p>"""
    multi_az: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether the reservation applies to Multi-AZ deployments.</p>"""
    state: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The state of the reserved DB instance.</p>"""
    recurring_charges: NotRequired[
        "aws_sdk_rds.types.recurring_charge_list.RecurringChargeList"
    ]
    """<p>The recurring price charged to run this reserved DB instance.</p>"""
    reserved_db_instance_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the reserved DB instance.</p>"""
    lease_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The unique identifier for the lease associated with the reserved DB instance.</p> <note> <p>Amazon Web Services Support might request the lease ID for an issue related to a reserved DB instance.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstance, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "reserved_db_instance_id" in value:
        pairs.append(
            (f"{prefix}.ReservedDBInstanceId", str(value["reserved_db_instance_id"]))
        )
    if "reserved_db_instances_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedDBInstancesOfferingId",
                str(value["reserved_db_instances_offering_id"]),
            )
        )
    if "db_instance_class" in value:
        pairs.append((f"{prefix}.DBInstanceClass", str(value["db_instance_class"])))
    if "start_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "fixed_price" in value:
        pairs.append((f"{prefix}.FixedPrice", str(value["fixed_price"])))
    if "usage_price" in value:
        pairs.append((f"{prefix}.UsagePrice", str(value["usage_price"])))
    if "currency_code" in value:
        pairs.append((f"{prefix}.CurrencyCode", str(value["currency_code"])))
    if "db_instance_count" in value:
        pairs.append((f"{prefix}.DBInstanceCount", str(value["db_instance_count"])))
    if "product_description" in value:
        pairs.append(
            (f"{prefix}.ProductDescription", str(value["product_description"]))
        )
    if "offering_type" in value:
        pairs.append((f"{prefix}.OfferingType", str(value["offering_type"])))
    if "multi_az" in value:
        pairs.append((f"{prefix}.MultiAZ", "true" if value["multi_az"] else "false"))
    if "state" in value:
        pairs.append((f"{prefix}.State", str(value["state"])))
    if "recurring_charges" in value:
        import aws_sdk_rds.types.recurring_charge_list

        aws_sdk_rds.types.recurring_charge_list.serialize_query(
            value["recurring_charges"], pairs, f"{prefix}.RecurringCharges"
        )
    if "reserved_db_instance_arn" in value:
        pairs.append(
            (f"{prefix}.ReservedDBInstanceArn", str(value["reserved_db_instance_arn"]))
        )
    if "lease_id" in value:
        pairs.append((f"{prefix}.LeaseId", str(value["lease_id"])))


def deserialize_query(el: Element) -> ReservedDBInstance:
    out: ReservedDBInstance = {}  # type: ignore[typeddict-item]
    child_reserved_db_instance_id = el.find("ReservedDBInstanceId")
    if child_reserved_db_instance_id is not None:
        out["reserved_db_instance_id"] = str(child_reserved_db_instance_id.text or "")
    child_reserved_db_instances_offering_id = el.find("ReservedDBInstancesOfferingId")
    if child_reserved_db_instances_offering_id is not None:
        out["reserved_db_instances_offering_id"] = str(
            child_reserved_db_instances_offering_id.text or ""
        )
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["start_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_start_time
        )
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
    child_db_instance_count = el.find("DBInstanceCount")
    if child_db_instance_count is not None:
        out["db_instance_count"] = int(child_db_instance_count.text or "")
    child_product_description = el.find("ProductDescription")
    if child_product_description is not None:
        out["product_description"] = str(child_product_description.text or "")
    child_offering_type = el.find("OfferingType")
    if child_offering_type is not None:
        out["offering_type"] = str(child_offering_type.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_state = el.find("State")
    if child_state is not None:
        out["state"] = str(child_state.text or "")
    child_recurring_charges = el.find("RecurringCharges")
    if child_recurring_charges is not None:
        import aws_sdk_rds.types.recurring_charge_list

        out["recurring_charges"] = (
            aws_sdk_rds.types.recurring_charge_list.deserialize_query(
                child_recurring_charges
            )
        )
    child_reserved_db_instance_arn = el.find("ReservedDBInstanceArn")
    if child_reserved_db_instance_arn is not None:
        out["reserved_db_instance_arn"] = str(child_reserved_db_instance_arn.text or "")
    child_lease_id = el.find("LeaseId")
    if child_lease_id is not None:
        out["lease_id"] = str(child_lease_id.text or "")
    return out

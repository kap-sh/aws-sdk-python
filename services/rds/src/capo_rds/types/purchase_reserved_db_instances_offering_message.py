"""Generated from Smithy shape ``com.amazonaws.rds#PurchaseReservedDBInstancesOfferingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer_optional
    import capo_rds.types.string
    import capo_rds.types.tag_list


class PurchaseReservedDBInstancesOfferingMessage(TypedDict, closed=True):
    reserved_db_instances_offering_id: NotRequired["capo_rds.types.string.String"]
    """<p>The ID of the Reserved DB instance offering to purchase.</p> <p>Example: 438012d3-4052-4cc7-b2e3-8d3372e0e706</p>"""
    reserved_db_instance_id: NotRequired["capo_rds.types.string.String"]
    """<p>Customer-specified identifier to track this reservation.</p> <p>Example: myreservationID</p>"""
    db_instance_count: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The number of instances to reserve.</p> <p>Default: <code>1</code> </p>"""
    tags: NotRequired["capo_rds.types.tag_list.TagList"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PurchaseReservedDBInstancesOfferingMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_db_instances_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}ReservedDBInstancesOfferingId",
                str(value["reserved_db_instances_offering_id"]),
            )
        )
    if "reserved_db_instance_id" in value:
        pairs.append(
            (f"{key_prefix}ReservedDBInstanceId", str(value["reserved_db_instance_id"]))
        )
    if "db_instance_count" in value:
        pairs.append((f"{key_prefix}DBInstanceCount", str(value["db_instance_count"])))
    if "tags" in value:
        import capo_rds.types.tag_list

        capo_rds.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> PurchaseReservedDBInstancesOfferingMessage:
    out: PurchaseReservedDBInstancesOfferingMessage = {}  # type: ignore[typeddict-item]
    child_reserved_db_instances_offering_id = el.find("ReservedDBInstancesOfferingId")
    if child_reserved_db_instances_offering_id is not None:
        out["reserved_db_instances_offering_id"] = str(
            child_reserved_db_instances_offering_id.text or ""
        )
    child_reserved_db_instance_id = el.find("ReservedDBInstanceId")
    if child_reserved_db_instance_id is not None:
        out["reserved_db_instance_id"] = str(child_reserved_db_instance_id.text or "")
    child_db_instance_count = el.find("DBInstanceCount")
    if child_db_instance_count is not None:
        out["db_instance_count"] = int(child_db_instance_count.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_rds.types.tag_list

        out["tags"] = capo_rds.types.tag_list.deserialize_query(child_tags)
    return out

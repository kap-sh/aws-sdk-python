"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstancesOfferingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.reserved_db_instances_offering_list
    import capo_rds.types.string


class ReservedDBInstancesOfferingMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    reserved_db_instances_offerings: NotRequired[
        "capo_rds.types.reserved_db_instances_offering_list.ReservedDBInstancesOfferingList"
    ]
    """<p>A list of reserved DB instance offerings.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstancesOfferingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "reserved_db_instances_offerings" in value:
        import capo_rds.types.reserved_db_instances_offering_list

        capo_rds.types.reserved_db_instances_offering_list.serialize_query(
            value["reserved_db_instances_offerings"],
            pairs,
            f"{key_prefix}ReservedDBInstancesOfferings",
        )


def deserialize_query(el: Element) -> ReservedDBInstancesOfferingMessage:
    out: ReservedDBInstancesOfferingMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_db_instances_offerings = el.find("ReservedDBInstancesOfferings")
    if child_reserved_db_instances_offerings is not None:
        import capo_rds.types.reserved_db_instances_offering_list

        out["reserved_db_instances_offerings"] = (
            capo_rds.types.reserved_db_instances_offering_list.deserialize_query(
                child_reserved_db_instances_offerings
            )
        )
    return out

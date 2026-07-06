"""Generated from Smithy shape ``com.amazonaws.rds#ReservedDBInstanceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.reserved_db_instance_list
    import aws_sdk_rds.types.string


class ReservedDBInstanceMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    reserved_db_instances: NotRequired[
        "aws_sdk_rds.types.reserved_db_instance_list.ReservedDBInstanceList"
    ]
    """<p>A list of reserved DB instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedDBInstanceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "reserved_db_instances" in value:
        import aws_sdk_rds.types.reserved_db_instance_list

        aws_sdk_rds.types.reserved_db_instance_list.serialize_query(
            value["reserved_db_instances"], pairs, f"{prefix}.ReservedDBInstances"
        )


def deserialize_query(el: Element) -> ReservedDBInstanceMessage:
    out: ReservedDBInstanceMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_reserved_db_instances = el.find("ReservedDBInstances")
    if child_reserved_db_instances is not None:
        import aws_sdk_rds.types.reserved_db_instance_list

        out["reserved_db_instances"] = (
            aws_sdk_rds.types.reserved_db_instance_list.deserialize_query(
                child_reserved_db_instances
            )
        )
    return out

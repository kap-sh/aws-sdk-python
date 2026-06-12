"""Generated from Smithy shape ``com.amazonaws.rds#OrderableDBInstanceOptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.orderable_db_instance_options_list
    import aws_sdk_rds.types.string


class OrderableDBInstanceOptionsMessage(TypedDict):
    orderable_db_instance_options: NotRequired[
        "aws_sdk_rds.types.orderable_db_instance_options_list.OrderableDBInstanceOptionsList"
    ]
    """<p>An <code>OrderableDBInstanceOption</code> structure containing information about orderable options for the DB instance.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "orderable_db_instance_options" in value:
        import aws_sdk_rds.types.orderable_db_instance_options_list

        aws_sdk_rds.types.orderable_db_instance_options_list.serialize_query(
            value["orderable_db_instance_options"],
            pairs,
            f"{prefix}.OrderableDBInstanceOptions",
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> OrderableDBInstanceOptionsMessage:
    out: OrderableDBInstanceOptionsMessage = {}  # type: ignore[typeddict-item]
    child_orderable_db_instance_options = el.find("OrderableDBInstanceOptions")
    if child_orderable_db_instance_options is not None:
        import aws_sdk_rds.types.orderable_db_instance_options_list

        out["orderable_db_instance_options"] = (
            aws_sdk_rds.types.orderable_db_instance_options_list.deserialize_query(
                child_orderable_db_instance_options
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

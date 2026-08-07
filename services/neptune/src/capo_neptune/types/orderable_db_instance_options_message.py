"""Generated from Smithy shape ``com.amazonaws.neptune#OrderableDBInstanceOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.orderable_db_instance_options_list
    import capo_neptune.types.string


class OrderableDBInstanceOptionsMessage(TypedDict, closed=True):
    orderable_db_instance_options: NotRequired[
        "capo_neptune.types.orderable_db_instance_options_list.OrderableDBInstanceOptionsList"
    ]
    """<p>An <a>OrderableDBInstanceOption</a> structure containing information about orderable options for the DB instance.</p>"""
    marker: NotRequired["capo_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code> .</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OrderableDBInstanceOptionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "orderable_db_instance_options" in value:
        import capo_neptune.types.orderable_db_instance_options_list

        capo_neptune.types.orderable_db_instance_options_list.serialize_query(
            value["orderable_db_instance_options"],
            pairs,
            f"{key_prefix}OrderableDBInstanceOptions",
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> OrderableDBInstanceOptionsMessage:
    out: OrderableDBInstanceOptionsMessage = {}  # type: ignore[typeddict-item]
    child_orderable_db_instance_options = el.find("OrderableDBInstanceOptions")
    if child_orderable_db_instance_options is not None:
        import capo_neptune.types.orderable_db_instance_options_list

        out["orderable_db_instance_options"] = (
            capo_neptune.types.orderable_db_instance_options_list.deserialize_query(
                child_orderable_db_instance_options
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

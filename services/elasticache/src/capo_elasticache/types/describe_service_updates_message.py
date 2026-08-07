"""Generated from Smithy shape ``com.amazonaws.elasticache#DescribeServiceUpdatesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.service_update_status_list
    import capo_elasticache.types.string


class DescribeServiceUpdatesMessage(TypedDict, closed=True):
    service_update_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The unique ID of the service update</p>"""
    service_update_status: NotRequired[
        "capo_elasticache.types.service_update_status_list.ServiceUpdateStatusList"
    ]
    """<p>The status of the service update</p>"""
    max_records: NotRequired["capo_elasticache.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response</p>"""
    marker: NotRequired["capo_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeServiceUpdatesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_update_name" in value:
        pairs.append(
            (f"{key_prefix}ServiceUpdateName", str(value["service_update_name"]))
        )
    if "service_update_status" in value:
        import capo_elasticache.types.service_update_status_list

        capo_elasticache.types.service_update_status_list.serialize_query(
            value["service_update_status"], pairs, f"{key_prefix}ServiceUpdateStatus"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeServiceUpdatesMessage:
    out: DescribeServiceUpdatesMessage = {}  # type: ignore[typeddict-item]
    child_service_update_name = el.find("ServiceUpdateName")
    if child_service_update_name is not None:
        out["service_update_name"] = str(child_service_update_name.text or "")
    child_service_update_status = el.find("ServiceUpdateStatus")
    if child_service_update_status is not None:
        import capo_elasticache.types.service_update_status_list

        out["service_update_status"] = (
            capo_elasticache.types.service_update_status_list.deserialize_query(
                child_service_update_status
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

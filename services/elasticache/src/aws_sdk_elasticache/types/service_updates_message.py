"""Generated from Smithy shape ``com.amazonaws.elasticache#ServiceUpdatesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.service_update_list
    import aws_sdk_elasticache.types.string


class ServiceUpdatesMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>An optional marker returned from a prior request. Use this marker for pagination of results from this operation. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    service_updates: NotRequired[
        "aws_sdk_elasticache.types.service_update_list.ServiceUpdateList"
    ]
    """<p>A list of service updates</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceUpdatesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "service_updates" in value:
        import aws_sdk_elasticache.types.service_update_list

        aws_sdk_elasticache.types.service_update_list.serialize_query(
            value["service_updates"], pairs, f"{prefix}.ServiceUpdates"
        )


def deserialize_query(el: Element) -> ServiceUpdatesMessage:
    out: ServiceUpdatesMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_service_updates = el.find("ServiceUpdates")
    if child_service_updates is not None:
        import aws_sdk_elasticache.types.service_update_list

        out["service_updates"] = (
            aws_sdk_elasticache.types.service_update_list.deserialize_query(
                child_service_updates
            )
        )
    return out

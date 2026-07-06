"""Generated from Smithy shape ``com.amazonaws.redshift#GetReservedNodeExchangeConfigurationOptionsInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.reserved_node_exchange_action_type
    import aws_sdk_redshift.types.string


class GetReservedNodeExchangeConfigurationOptionsInputMessage(TypedDict, closed=True):
    action_type: NotRequired[
        "aws_sdk_redshift.types.reserved_node_exchange_action_type.ReservedNodeExchangeActionType"
    ]
    """<p>The action type of the reserved-node configuration. The action type can be an exchange initiated from either a snapshot or a resize.</p>"""
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier for the cluster that is the source for a reserved-node exchange.</p>"""
    snapshot_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier for the snapshot that is the source for the reserved-node exchange.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>Marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>GetReservedNodeExchangeConfigurationOptions</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetReservedNodeExchangeConfigurationOptionsInputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "action_type" in value:
        import aws_sdk_redshift.types.reserved_node_exchange_action_type

        aws_sdk_redshift.types.reserved_node_exchange_action_type.serialize_query(
            value["action_type"], pairs, f"{prefix}.ActionType"
        )
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(
    el: Element,
) -> GetReservedNodeExchangeConfigurationOptionsInputMessage:
    out: GetReservedNodeExchangeConfigurationOptionsInputMessage = {}  # type: ignore[typeddict-item]
    child_action_type = el.find("ActionType")
    if child_action_type is not None:
        import aws_sdk_redshift.types.reserved_node_exchange_action_type

        out["action_type"] = (
            aws_sdk_redshift.types.reserved_node_exchange_action_type.deserialize_query(
                child_action_type
            )
        )
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeSnapshotSchedulesMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_key_list
    import aws_sdk_redshift.types.tag_value_list


class DescribeSnapshotSchedulesMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier for the cluster whose snapshot schedules you want to view.</p>"""
    schedule_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for a snapshot schedule.</p>"""
    tag_keys: NotRequired["aws_sdk_redshift.types.tag_key_list.TagKeyList"]
    """<p>The key value for a snapshot schedule tag.</p>"""
    tag_values: NotRequired["aws_sdk_redshift.types.tag_value_list.TagValueList"]
    """<p>The value corresponding to the key of the snapshot schedule tag.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>marker</code> parameter and retrying the command. If the <code>marker</code> field is empty, all response records have been retrieved for the request.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number or response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned <code>marker</code> value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSnapshotSchedulesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "schedule_identifier" in value:
        pairs.append(
            (f"{prefix}.ScheduleIdentifier", str(value["schedule_identifier"]))
        )
    if "tag_keys" in value:
        import aws_sdk_redshift.types.tag_key_list

        aws_sdk_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{prefix}.TagKeys"
        )
    if "tag_values" in value:
        import aws_sdk_redshift.types.tag_value_list

        aws_sdk_redshift.types.tag_value_list.serialize_query(
            value["tag_values"], pairs, f"{prefix}.TagValues"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeSnapshotSchedulesMessage:
    out: DescribeSnapshotSchedulesMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_redshift.types.tag_key_list

        out["tag_keys"] = aws_sdk_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    child_tag_values = el.find("TagValues")
    if child_tag_values is not None:
        import aws_sdk_redshift.types.tag_value_list

        out["tag_values"] = aws_sdk_redshift.types.tag_value_list.deserialize_query(
            child_tag_values
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out

"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.associated_cluster_list
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.schedule_definition_list
    import aws_sdk_redshift.types.scheduled_snapshot_time_list
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_list


class SnapshotSchedule(TypedDict):
    schedule_definitions: NotRequired[
        "aws_sdk_redshift.types.schedule_definition_list.ScheduleDefinitionList"
    ]
    """<p>A list of ScheduleDefinitions.</p>"""
    schedule_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>A unique identifier for the schedule.</p>"""
    schedule_description: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The description of the schedule.</p>"""
    tags: NotRequired["aws_sdk_redshift.types.tag_list.TagList"]
    """<p>An optional set of tags describing the schedule.</p>"""
    next_invocations: NotRequired[
        "aws_sdk_redshift.types.scheduled_snapshot_time_list.ScheduledSnapshotTimeList"
    ]
    """<p></p>"""
    associated_cluster_count: NotRequired[
        "aws_sdk_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of clusters associated with the schedule.</p>"""
    associated_clusters: NotRequired[
        "aws_sdk_redshift.types.associated_cluster_list.AssociatedClusterList"
    ]
    """<p>A list of clusters associated with the schedule. A maximum of 100 clusters is returned.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotSchedule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "schedule_definitions" in value:
        import aws_sdk_redshift.types.schedule_definition_list

        aws_sdk_redshift.types.schedule_definition_list.serialize_query(
            value["schedule_definitions"], pairs, f"{prefix}.ScheduleDefinitions"
        )
    if "schedule_identifier" in value:
        pairs.append(
            (f"{prefix}.ScheduleIdentifier", str(value["schedule_identifier"]))
        )
    if "schedule_description" in value:
        pairs.append(
            (f"{prefix}.ScheduleDescription", str(value["schedule_description"]))
        )
    if "tags" in value:
        import aws_sdk_redshift.types.tag_list

        aws_sdk_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "next_invocations" in value:
        import aws_sdk_redshift.types.scheduled_snapshot_time_list

        aws_sdk_redshift.types.scheduled_snapshot_time_list.serialize_query(
            value["next_invocations"], pairs, f"{prefix}.NextInvocations"
        )
    if "associated_cluster_count" in value:
        pairs.append(
            (f"{prefix}.AssociatedClusterCount", str(value["associated_cluster_count"]))
        )
    if "associated_clusters" in value:
        import aws_sdk_redshift.types.associated_cluster_list

        aws_sdk_redshift.types.associated_cluster_list.serialize_query(
            value["associated_clusters"], pairs, f"{prefix}.AssociatedClusters"
        )


def deserialize_query(el: Element) -> SnapshotSchedule:
    out: SnapshotSchedule = {}  # type: ignore[typeddict-item]
    child_schedule_definitions = el.find("ScheduleDefinitions")
    if child_schedule_definitions is not None:
        import aws_sdk_redshift.types.schedule_definition_list

        out["schedule_definitions"] = (
            aws_sdk_redshift.types.schedule_definition_list.deserialize_query(
                child_schedule_definitions
            )
        )
    child_schedule_identifier = el.find("ScheduleIdentifier")
    if child_schedule_identifier is not None:
        out["schedule_identifier"] = str(child_schedule_identifier.text or "")
    child_schedule_description = el.find("ScheduleDescription")
    if child_schedule_description is not None:
        out["schedule_description"] = str(child_schedule_description.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_redshift.types.tag_list

        out["tags"] = aws_sdk_redshift.types.tag_list.deserialize_query(child_tags)
    child_next_invocations = el.find("NextInvocations")
    if child_next_invocations is not None:
        import aws_sdk_redshift.types.scheduled_snapshot_time_list

        out["next_invocations"] = (
            aws_sdk_redshift.types.scheduled_snapshot_time_list.deserialize_query(
                child_next_invocations
            )
        )
    child_associated_cluster_count = el.find("AssociatedClusterCount")
    if child_associated_cluster_count is not None:
        out["associated_cluster_count"] = int(child_associated_cluster_count.text or "")
    child_associated_clusters = el.find("AssociatedClusters")
    if child_associated_clusters is not None:
        import aws_sdk_redshift.types.associated_cluster_list

        out["associated_clusters"] = (
            aws_sdk_redshift.types.associated_cluster_list.deserialize_query(
                child_associated_clusters
            )
        )
    return out

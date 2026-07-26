"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeScheduledActionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.integer_optional
    import capo_redshift.types.scheduled_action_filter_list
    import capo_redshift.types.scheduled_action_type_values
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp


class DescribeScheduledActionsMessage(TypedDict, closed=True):
    scheduled_action_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the scheduled action to retrieve. </p>"""
    target_action_type: NotRequired[
        "capo_redshift.types.scheduled_action_type_values.ScheduledActionTypeValues"
    ]
    """<p>The type of the scheduled actions to retrieve. </p>"""
    start_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.</p>"""
    end_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.</p>"""
    active: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions. </p>"""
    filters: NotRequired[
        "capo_redshift.types.scheduled_action_filter_list.ScheduledActionFilterList"
    ]
    """<p>List of scheduled action filters. </p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeScheduledActions</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeScheduledActionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{prefix}.ScheduledActionName", str(value["scheduled_action_name"]))
        )
    if "target_action_type" in value:
        import capo_redshift.types.scheduled_action_type_values

        capo_redshift.types.scheduled_action_type_values.serialize_query(
            value["target_action_type"], pairs, f"{prefix}.TargetActionType"
        )
    if "start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "active" in value:
        pairs.append((f"{prefix}.Active", "true" if value["active"] else "false"))
    if "filters" in value:
        import capo_redshift.types.scheduled_action_filter_list

        capo_redshift.types.scheduled_action_filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeScheduledActionsMessage:
    out: DescribeScheduledActionsMessage = {}  # type: ignore[typeddict-item]
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    child_target_action_type = el.find("TargetActionType")
    if child_target_action_type is not None:
        import capo_redshift.types.scheduled_action_type_values

        out["target_action_type"] = (
            capo_redshift.types.scheduled_action_type_values.deserialize_query(
                child_target_action_type
            )
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_redshift.types.t_stamp

        out["start_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_redshift.types.t_stamp

        out["end_time"] = capo_redshift.types.t_stamp.deserialize_query(child_end_time)
    child_active = el.find("Active")
    if child_active is not None:
        out["active"] = (child_active.text or "").lower() == "true"
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_redshift.types.scheduled_action_filter_list

        out["filters"] = (
            capo_redshift.types.scheduled_action_filter_list.deserialize_query(
                child_filters
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out

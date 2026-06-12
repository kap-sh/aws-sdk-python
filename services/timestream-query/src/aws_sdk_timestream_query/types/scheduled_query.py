"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.error_report_configuration
    import aws_sdk_timestream_query.types.scheduled_query_name
    import aws_sdk_timestream_query.types.scheduled_query_run_status
    import aws_sdk_timestream_query.types.scheduled_query_state
    import aws_sdk_timestream_query.types.target_destination
    import aws_sdk_timestream_query.types.time


class ScheduledQuery(TypedDict):
    arn: "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name.</p>"""
    name: "aws_sdk_timestream_query.types.scheduled_query_name.ScheduledQueryName"
    """<p>The name of the scheduled query.</p>"""
    creation_time: NotRequired["aws_sdk_timestream_query.types.time.Time"]
    """<p>The creation time of the scheduled query.</p>"""
    state: "aws_sdk_timestream_query.types.scheduled_query_state.ScheduledQueryState"
    """<p>State of scheduled query. </p>"""
    previous_invocation_time: NotRequired["aws_sdk_timestream_query.types.time.Time"]
    """<p>The last time the scheduled query was run.</p>"""
    next_invocation_time: NotRequired["aws_sdk_timestream_query.types.time.Time"]
    """<p>The next time the scheduled query is to be run.</p>"""
    error_report_configuration: NotRequired[
        "aws_sdk_timestream_query.types.error_report_configuration.ErrorReportConfiguration"
    ]
    """<p>Configuration for scheduled query error reporting.</p>"""
    target_destination: NotRequired[
        "aws_sdk_timestream_query.types.target_destination.TargetDestination"
    ]
    """<p>Target data source where final scheduled query result will be written.</p>"""
    last_run_status: NotRequired[
        "aws_sdk_timestream_query.types.scheduled_query_run_status.ScheduledQueryRunStatus"
    ]
    """<p>Status of the last scheduled query run.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQuery) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    if "creation_time" in value:
        import aws_sdk_timestream_query.types.time

        out["CreationTime"] = (
            aws_sdk_timestream_query.types.time.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    import aws_sdk_timestream_query.types.scheduled_query_state

    out["State"] = (
        aws_sdk_timestream_query.types.scheduled_query_state.serialize_aws_json_1_0(
            value["state"]
        )
    )
    if "previous_invocation_time" in value:
        import aws_sdk_timestream_query.types.time

        out["PreviousInvocationTime"] = (
            aws_sdk_timestream_query.types.time.serialize_aws_json_1_0(
                value["previous_invocation_time"]
            )
        )
    if "next_invocation_time" in value:
        import aws_sdk_timestream_query.types.time

        out["NextInvocationTime"] = (
            aws_sdk_timestream_query.types.time.serialize_aws_json_1_0(
                value["next_invocation_time"]
            )
        )
    if "error_report_configuration" in value:
        import aws_sdk_timestream_query.types.error_report_configuration

        out["ErrorReportConfiguration"] = (
            aws_sdk_timestream_query.types.error_report_configuration.serialize_aws_json_1_0(
                value["error_report_configuration"]
            )
        )
    if "target_destination" in value:
        import aws_sdk_timestream_query.types.target_destination

        out["TargetDestination"] = (
            aws_sdk_timestream_query.types.target_destination.serialize_aws_json_1_0(
                value["target_destination"]
            )
        )
    if "last_run_status" in value:
        import aws_sdk_timestream_query.types.scheduled_query_run_status

        out["LastRunStatus"] = (
            aws_sdk_timestream_query.types.scheduled_query_run_status.serialize_aws_json_1_0(
                value["last_run_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQuery:
    out: ScheduledQuery = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ScheduledQuery.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ScheduledQuery.name required")
    if "CreationTime" in data:
        import aws_sdk_timestream_query.types.time

        out["creation_time"] = (
            aws_sdk_timestream_query.types.time.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "State" in data:
        import aws_sdk_timestream_query.types.scheduled_query_state

        out["state"] = (
            aws_sdk_timestream_query.types.scheduled_query_state.deserialize_aws_json_1_0(
                data["State"]
            )
        )
    else:
        raise DeserializationError("ScheduledQuery.state required")
    if "PreviousInvocationTime" in data:
        import aws_sdk_timestream_query.types.time

        out["previous_invocation_time"] = (
            aws_sdk_timestream_query.types.time.deserialize_aws_json_1_0(
                data["PreviousInvocationTime"]
            )
        )
    if "NextInvocationTime" in data:
        import aws_sdk_timestream_query.types.time

        out["next_invocation_time"] = (
            aws_sdk_timestream_query.types.time.deserialize_aws_json_1_0(
                data["NextInvocationTime"]
            )
        )
    if "ErrorReportConfiguration" in data:
        import aws_sdk_timestream_query.types.error_report_configuration

        out["error_report_configuration"] = (
            aws_sdk_timestream_query.types.error_report_configuration.deserialize_aws_json_1_0(
                data["ErrorReportConfiguration"]
            )
        )
    if "TargetDestination" in data:
        import aws_sdk_timestream_query.types.target_destination

        out["target_destination"] = (
            aws_sdk_timestream_query.types.target_destination.deserialize_aws_json_1_0(
                data["TargetDestination"]
            )
        )
    if "LastRunStatus" in data:
        import aws_sdk_timestream_query.types.scheduled_query_run_status

        out["last_run_status"] = (
            aws_sdk_timestream_query.types.scheduled_query_run_status.deserialize_aws_json_1_0(
                data["LastRunStatus"]
            )
        )
    return out

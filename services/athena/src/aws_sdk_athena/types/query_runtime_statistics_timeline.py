"""Generated from Smithy shape ``com.amazonaws.athena#QueryRuntimeStatisticsTimeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.long


class QueryRuntimeStatisticsTimeline(TypedDict, closed=True):
    query_queue_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of milliseconds that the query was in your query queue waiting for resources. Note that if transient errors occur, Athena might automatically add the query back to the queue.</p>"""
    service_pre_processing_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p> The number of milliseconds that Athena spends on preprocessing before it submits the query to the engine. </p>"""
    query_planning_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source. Note that because the query engine performs the query planning, query planning time is a subset of engine processing time.</p>"""
    engine_execution_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of milliseconds that the query took to execute.</p>"""
    service_processing_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to finalize and publish the query results after the query engine finished running the query.</p>"""
    total_execution_time_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The number of milliseconds that Athena took to run the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryRuntimeStatisticsTimeline) -> dict:
    out: dict = {}
    if "query_queue_time_in_millis" in value:
        out["QueryQueueTimeInMillis"] = value["query_queue_time_in_millis"]
    if "service_pre_processing_time_in_millis" in value:
        out["ServicePreProcessingTimeInMillis"] = value[
            "service_pre_processing_time_in_millis"
        ]
    if "query_planning_time_in_millis" in value:
        out["QueryPlanningTimeInMillis"] = value["query_planning_time_in_millis"]
    if "engine_execution_time_in_millis" in value:
        out["EngineExecutionTimeInMillis"] = value["engine_execution_time_in_millis"]
    if "service_processing_time_in_millis" in value:
        out["ServiceProcessingTimeInMillis"] = value[
            "service_processing_time_in_millis"
        ]
    if "total_execution_time_in_millis" in value:
        out["TotalExecutionTimeInMillis"] = value["total_execution_time_in_millis"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryRuntimeStatisticsTimeline:
    out: QueryRuntimeStatisticsTimeline = {}  # type: ignore[typeddict-item]
    if "QueryQueueTimeInMillis" in data:
        out["query_queue_time_in_millis"] = data["QueryQueueTimeInMillis"]
    if "ServicePreProcessingTimeInMillis" in data:
        out["service_pre_processing_time_in_millis"] = data[
            "ServicePreProcessingTimeInMillis"
        ]
    if "QueryPlanningTimeInMillis" in data:
        out["query_planning_time_in_millis"] = data["QueryPlanningTimeInMillis"]
    if "EngineExecutionTimeInMillis" in data:
        out["engine_execution_time_in_millis"] = data["EngineExecutionTimeInMillis"]
    if "ServiceProcessingTimeInMillis" in data:
        out["service_processing_time_in_millis"] = data["ServiceProcessingTimeInMillis"]
    if "TotalExecutionTimeInMillis" in data:
        out["total_execution_time_in_millis"] = data["TotalExecutionTimeInMillis"]
    return out

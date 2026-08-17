"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ScheduledQueryDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.action_status
    import capo_cloudwatch_logs.types.scheduled_query_destination_type
    import capo_cloudwatch_logs.types.string


class ScheduledQueryDestination(TypedDict, closed=True):
    destination_type: NotRequired[
        "capo_cloudwatch_logs.types.scheduled_query_destination_type.ScheduledQueryDestinationType"
    ]
    """<p>The type of destination for query results.</p>"""
    destination_identifier: NotRequired["capo_cloudwatch_logs.types.string.String"]
    """<p>The identifier for the destination where results are delivered.</p>"""
    status: NotRequired["capo_cloudwatch_logs.types.action_status.ActionStatus"]
    """<p>The processing status of the destination delivery.</p>"""
    processed_identifier: NotRequired["capo_cloudwatch_logs.types.string.String"]
    """<p>The identifier of the processed result at the destination.</p>"""
    error_message: NotRequired["capo_cloudwatch_logs.types.string.String"]
    """<p>Error message if destination processing failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledQueryDestination) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import capo_cloudwatch_logs.types.scheduled_query_destination_type

        out["destinationType"] = (
            capo_cloudwatch_logs.types.scheduled_query_destination_type.serialize_aws_json_1_1(
                value["destination_type"]
            )
        )
    if "destination_identifier" in value:
        out["destinationIdentifier"] = value["destination_identifier"]
    if "status" in value:
        import capo_cloudwatch_logs.types.action_status

        out["status"] = capo_cloudwatch_logs.types.action_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "processed_identifier" in value:
        out["processedIdentifier"] = value["processed_identifier"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduledQueryDestination:
    out: ScheduledQueryDestination = {}  # type: ignore[typeddict-item]
    if data.get("destinationType") is not None:
        import capo_cloudwatch_logs.types.scheduled_query_destination_type

        out["destination_type"] = (
            capo_cloudwatch_logs.types.scheduled_query_destination_type.deserialize_aws_json_1_1(
                data["destinationType"]
            )
        )
    if data.get("destinationIdentifier") is not None:
        out["destination_identifier"] = data["destinationIdentifier"]
    if data.get("status") is not None:
        import capo_cloudwatch_logs.types.action_status

        out["status"] = (
            capo_cloudwatch_logs.types.action_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("processedIdentifier") is not None:
        out["processed_identifier"] = data["processedIdentifier"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out

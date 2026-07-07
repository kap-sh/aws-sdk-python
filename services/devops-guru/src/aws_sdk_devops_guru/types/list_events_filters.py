"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListEventsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.event_class
    import aws_sdk_devops_guru.types.event_data_source
    import aws_sdk_devops_guru.types.event_source
    import aws_sdk_devops_guru.types.event_time_range
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.resource_collection


class ListEventsFilters(TypedDict, closed=True):
    insight_id: NotRequired["aws_sdk_devops_guru.types.insight_id.InsightId"]
    """<p> An ID of an insight that is related to the events you want to filter for. </p>"""
    event_time_range: NotRequired[
        "aws_sdk_devops_guru.types.event_time_range.EventTimeRange"
    ]
    """<p> A time range during which you want the filtered events to have occurred. </p>"""
    event_class: NotRequired["aws_sdk_devops_guru.types.event_class.EventClass"]
    """<p> The class of the events you want to filter for, such as an infrastructure change, a deployment, or a schema change. </p>"""
    event_source: NotRequired["aws_sdk_devops_guru.types.event_source.EventSource"]
    """<p> The Amazon Web Services source that emitted the events you want to filter for. </p>"""
    data_source: NotRequired[
        "aws_sdk_devops_guru.types.event_data_source.EventDataSource"
    ]
    """<p> The source, <code>AWS_CLOUD_TRAIL</code> or <code>AWS_CODE_DEPLOY</code>, of the events you want returned. </p>"""
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListEventsFilters) -> dict:
    out: dict = {}
    if "insight_id" in value:
        out["InsightId"] = value["insight_id"]
    if "event_time_range" in value:
        import aws_sdk_devops_guru.types.event_time_range

        out["EventTimeRange"] = (
            aws_sdk_devops_guru.types.event_time_range.serialize_json(
                value["event_time_range"]
            )
        )
    if "event_class" in value:
        import aws_sdk_devops_guru.types.event_class

        out["EventClass"] = aws_sdk_devops_guru.types.event_class.serialize_json(
            value["event_class"]
        )
    if "event_source" in value:
        out["EventSource"] = value["event_source"]
    if "data_source" in value:
        import aws_sdk_devops_guru.types.event_data_source

        out["DataSource"] = aws_sdk_devops_guru.types.event_data_source.serialize_json(
            value["data_source"]
        )
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEventsFilters:
    out: ListEventsFilters = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    if "EventTimeRange" in data:
        import aws_sdk_devops_guru.types.event_time_range

        out["event_time_range"] = (
            aws_sdk_devops_guru.types.event_time_range.deserialize_json(
                data["EventTimeRange"]
            )
        )
    if "EventClass" in data:
        import aws_sdk_devops_guru.types.event_class

        out["event_class"] = aws_sdk_devops_guru.types.event_class.deserialize_json(
            data["EventClass"]
        )
    if "EventSource" in data:
        out["event_source"] = data["EventSource"]
    if "DataSource" in data:
        import aws_sdk_devops_guru.types.event_data_source

        out["data_source"] = (
            aws_sdk_devops_guru.types.event_data_source.deserialize_json(
                data["DataSource"]
            )
        )
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.devopsguru#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.event_class
    import aws_sdk_devops_guru.types.event_data_source
    import aws_sdk_devops_guru.types.event_id
    import aws_sdk_devops_guru.types.event_name
    import aws_sdk_devops_guru.types.event_resources
    import aws_sdk_devops_guru.types.event_source
    import aws_sdk_devops_guru.types.resource_collection
    import aws_sdk_devops_guru.types.timestamp


class Event(TypedDict, closed=True):
    resource_collection: NotRequired[
        "aws_sdk_devops_guru.types.resource_collection.ResourceCollection"
    ]
    id: NotRequired["aws_sdk_devops_guru.types.event_id.EventId"]
    """<p> The ID of the event. </p>"""
    time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> A <code>Timestamp</code> that specifies the time the event occurred. </p>"""
    event_source: NotRequired["aws_sdk_devops_guru.types.event_source.EventSource"]
    """<p> The Amazon Web Services source that emitted the event. </p>"""
    name: NotRequired["aws_sdk_devops_guru.types.event_name.EventName"]
    """<p> The name of the event. </p>"""
    data_source: NotRequired[
        "aws_sdk_devops_guru.types.event_data_source.EventDataSource"
    ]
    """<p> The source, <code>AWS_CLOUD_TRAIL</code> or <code>AWS_CODE_DEPLOY</code>, where DevOps Guru analysis found the event. </p>"""
    event_class: NotRequired["aws_sdk_devops_guru.types.event_class.EventClass"]
    """<p> The class of the event. The class specifies what the event is related to, such as an infrastructure change, a deployment, or a schema change. </p>"""
    resources: NotRequired["aws_sdk_devops_guru.types.event_resources.EventResources"]
    """<p> An <code>EventResource</code> object that contains information about the resource that emitted the event. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Event) -> dict:
    out: dict = {}
    if "resource_collection" in value:
        import aws_sdk_devops_guru.types.resource_collection

        out["ResourceCollection"] = (
            aws_sdk_devops_guru.types.resource_collection.serialize_json(
                value["resource_collection"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["Time"] = aws_sdk_devops_guru.types.timestamp.serialize_json(value["time"])
    if "event_source" in value:
        out["EventSource"] = value["event_source"]
    if "name" in value:
        out["Name"] = value["name"]
    if "data_source" in value:
        import aws_sdk_devops_guru.types.event_data_source

        out["DataSource"] = aws_sdk_devops_guru.types.event_data_source.serialize_json(
            value["data_source"]
        )
    if "event_class" in value:
        import aws_sdk_devops_guru.types.event_class

        out["EventClass"] = aws_sdk_devops_guru.types.event_class.serialize_json(
            value["event_class"]
        )
    if "resources" in value:
        import aws_sdk_devops_guru.types.event_resources

        out["Resources"] = aws_sdk_devops_guru.types.event_resources.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "ResourceCollection" in data:
        import aws_sdk_devops_guru.types.resource_collection

        out["resource_collection"] = (
            aws_sdk_devops_guru.types.resource_collection.deserialize_json(
                data["ResourceCollection"]
            )
        )
    if "Id" in data:
        out["id"] = data["Id"]
    if "Time" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(data["Time"])
    if "EventSource" in data:
        out["event_source"] = data["EventSource"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DataSource" in data:
        import aws_sdk_devops_guru.types.event_data_source

        out["data_source"] = (
            aws_sdk_devops_guru.types.event_data_source.deserialize_json(
                data["DataSource"]
            )
        )
    if "EventClass" in data:
        import aws_sdk_devops_guru.types.event_class

        out["event_class"] = aws_sdk_devops_guru.types.event_class.deserialize_json(
            data["EventClass"]
        )
    if "Resources" in data:
        import aws_sdk_devops_guru.types.event_resources

        out["resources"] = aws_sdk_devops_guru.types.event_resources.deserialize_json(
            data["Resources"]
        )
    return out

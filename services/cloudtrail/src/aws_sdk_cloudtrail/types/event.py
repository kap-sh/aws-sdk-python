"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Event``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.date
    import aws_sdk_cloudtrail.types.resource_list
    import aws_sdk_cloudtrail.types.string


class Event(TypedDict):
    event_id: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The CloudTrail ID of the event returned.</p>"""
    event_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The name of the event returned.</p>"""
    read_only: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>Information about whether the event is a write event or a read event. </p>"""
    access_key_id: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Web Services access key ID that was used to sign the request. If the request was made with temporary security credentials, this is the access key ID of the temporary credentials.</p>"""
    event_time: NotRequired["aws_sdk_cloudtrail.types.date.Date"]
    """<p>The date and time of the event returned.</p>"""
    event_source: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Web Services service to which the request was made.</p>"""
    username: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>A user name or role name of the requester that called the API in the event returned.</p>"""
    resources: NotRequired["aws_sdk_cloudtrail.types.resource_list.ResourceList"]
    """<p>A list of resources referenced by the event returned.</p>"""
    cloud_trail_event: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>A JSON string that contains a representation of the event returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["EventId"] = value["event_id"]
    if "event_name" in value:
        out["EventName"] = value["event_name"]
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    if "access_key_id" in value:
        out["AccessKeyId"] = value["access_key_id"]
    if "event_time" in value:
        import aws_sdk_cloudtrail.types.date

        out["EventTime"] = aws_sdk_cloudtrail.types.date.serialize_aws_json_1_1(
            value["event_time"]
        )
    if "event_source" in value:
        out["EventSource"] = value["event_source"]
    if "username" in value:
        out["Username"] = value["username"]
    if "resources" in value:
        import aws_sdk_cloudtrail.types.resource_list

        out["Resources"] = (
            aws_sdk_cloudtrail.types.resource_list.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    if "cloud_trail_event" in value:
        out["CloudTrailEvent"] = value["cloud_trail_event"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "EventId" in data:
        out["event_id"] = data["EventId"]
    if "EventName" in data:
        out["event_name"] = data["EventName"]
    if "ReadOnly" in data:
        out["read_only"] = data["ReadOnly"]
    if "AccessKeyId" in data:
        out["access_key_id"] = data["AccessKeyId"]
    if "EventTime" in data:
        import aws_sdk_cloudtrail.types.date

        out["event_time"] = aws_sdk_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["EventTime"]
        )
    if "EventSource" in data:
        out["event_source"] = data["EventSource"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Resources" in data:
        import aws_sdk_cloudtrail.types.resource_list

        out["resources"] = (
            aws_sdk_cloudtrail.types.resource_list.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    if "CloudTrailEvent" in data:
        out["cloud_trail_event"] = data["CloudTrailEvent"]
    return out

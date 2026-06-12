"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetEventConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.string


class GetEventConfigurationRequest(TypedDict):
    trail_name: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The name of the trail for which you want to retrieve event configuration settings.</p>"""
    event_data_store: NotRequired["aws_sdk_cloudtrail.types.string.String"]
    """<p>The Amazon Resource Name (ARN) or ID suffix of the ARN of the event data store for which you want to retrieve event configuration settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventConfigurationRequest) -> dict:
    out: dict = {}
    if "trail_name" in value:
        out["TrailName"] = value["trail_name"]
    if "event_data_store" in value:
        out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventConfigurationRequest:
    out: GetEventConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "TrailName" in data:
        out["trail_name"] = data["TrailName"]
    if "EventDataStore" in data:
        out["event_data_store"] = data["EventDataStore"]
    return out

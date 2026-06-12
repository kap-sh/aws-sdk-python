"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerLogResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_log_event_list
    import aws_sdk_lightsail.types.string


class GetContainerLogResult(TypedDict):
    log_events: NotRequired[
        "aws_sdk_lightsail.types.container_service_log_event_list.ContainerServiceLogEventList"
    ]
    """<p>An array of objects that describe the log events of a container.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetContainerLog</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerLogResult) -> dict:
    out: dict = {}
    if "log_events" in value:
        import aws_sdk_lightsail.types.container_service_log_event_list

        out["logEvents"] = (
            aws_sdk_lightsail.types.container_service_log_event_list.serialize_aws_json_1_1(
                value["log_events"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerLogResult:
    out: GetContainerLogResult = {}  # type: ignore[typeddict-item]
    if "logEvents" in data:
        import aws_sdk_lightsail.types.container_service_log_event_list

        out["log_events"] = (
            aws_sdk_lightsail.types.container_service_log_event_list.deserialize_aws_json_1_1(
                data["logEvents"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out

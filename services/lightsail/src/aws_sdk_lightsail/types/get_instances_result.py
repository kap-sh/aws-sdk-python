"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstancesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.instance_list
    import aws_sdk_lightsail.types.string


class GetInstancesResult(TypedDict, closed=True):
    instances: NotRequired["aws_sdk_lightsail.types.instance_list.InstanceList"]
    """<p>An array of key-value pairs containing information about your instances.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetInstances</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstancesResult) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_lightsail.types.instance_list

        out["instances"] = aws_sdk_lightsail.types.instance_list.serialize_aws_json_1_1(
            value["instances"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstancesResult:
    out: GetInstancesResult = {}  # type: ignore[typeddict-item]
    if "instances" in data:
        import aws_sdk_lightsail.types.instance_list

        out["instances"] = (
            aws_sdk_lightsail.types.instance_list.deserialize_aws_json_1_1(
                data["instances"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out

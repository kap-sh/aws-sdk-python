"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.endpoint_name
    import aws_sdk_eventbridge.types.home_region


class DescribeEndpointRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.endpoint_name.EndpointName"
    r"""<p>The name of the endpoint you want to get information about. For example, <code>\"Name\":\"us-east-2-custom_bus_A-endpoint\"</code>.</p>"""
    home_region: NotRequired["aws_sdk_eventbridge.types.home_region.HomeRegion"]
    r"""<p>The primary Region of the endpoint you want to get information about. For example <code>\"HomeRegion\": \"us-east-1\"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointRequest:
    out: DescribeEndpointRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeEndpointRequest.name required")
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    return out

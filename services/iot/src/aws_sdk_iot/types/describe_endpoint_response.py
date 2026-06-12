"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.endpoint_address


class DescribeEndpointResponse(TypedDict):
    endpoint_address: NotRequired["aws_sdk_iot.types.endpoint_address.EndpointAddress"]
    """<p>The endpoint. The format of the endpoint is as follows: <i>identifier</i>.iot.<i>region</i>.amazonaws.com.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_address" in value:
        out["endpointAddress"] = value["endpoint_address"]
    return out


def deserialize_json(data: dict) -> DescribeEndpointResponse:
    out: DescribeEndpointResponse = {}  # type: ignore[typeddict-item]
    if "endpointAddress" in data:
        out["endpoint_address"] = data["endpointAddress"]
    return out

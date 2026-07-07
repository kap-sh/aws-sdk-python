"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class DescribeCustomRoutingEndpointGroupRequest(TypedDict, closed=True):
    endpoint_group_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingEndpointGroupRequest) -> dict:
    out: dict = {}
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingEndpointGroupRequest:
    out: DescribeCustomRoutingEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError(
            "DescribeCustomRoutingEndpointGroupRequest.endpoint_group_arn required"
        )
    return out

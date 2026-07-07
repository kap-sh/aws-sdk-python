"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCustomRoutingPortMappingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.port_mappings_max_results


class ListCustomRoutingPortMappingsRequest(TypedDict, closed=True):
    accelerator_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the accelerator to list the custom routing port mappings for.</p>"""
    endpoint_group_arn: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group to list the custom routing port mappings for.</p>"""
    max_results: NotRequired[
        "aws_sdk_global_accelerator.types.port_mappings_max_results.PortMappingsMaxResults"
    ]
    """<p>The number of destination port mappings that you want to return with this call. The default value is 10.</p>"""
    next_token: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCustomRoutingPortMappingsRequest) -> dict:
    out: dict = {}
    out["AcceleratorArn"] = value["accelerator_arn"]
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCustomRoutingPortMappingsRequest:
    out: ListCustomRoutingPortMappingsRequest = {}  # type: ignore[typeddict-item]
    if "AcceleratorArn" in data:
        out["accelerator_arn"] = data["AcceleratorArn"]
    else:
        raise DeserializationError(
            "ListCustomRoutingPortMappingsRequest.accelerator_arn required"
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

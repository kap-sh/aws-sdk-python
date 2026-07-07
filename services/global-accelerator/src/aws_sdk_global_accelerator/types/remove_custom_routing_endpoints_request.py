"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#RemoveCustomRoutingEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_ids
    import aws_sdk_global_accelerator.types.generic_string


class RemoveCustomRoutingEndpointsRequest(TypedDict, closed=True):
    endpoint_ids: "aws_sdk_global_accelerator.types.endpoint_ids.EndpointIds"
    """<p>The IDs for the endpoints. For custom routing accelerators, endpoint IDs are the virtual private cloud (VPC) subnet IDs. </p>"""
    endpoint_group_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group to remove endpoints from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveCustomRoutingEndpointsRequest) -> dict:
    out: dict = {}
    import aws_sdk_global_accelerator.types.endpoint_ids

    out["EndpointIds"] = (
        aws_sdk_global_accelerator.types.endpoint_ids.serialize_aws_json_1_1(
            value["endpoint_ids"]
        )
    )
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveCustomRoutingEndpointsRequest:
    out: RemoveCustomRoutingEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "EndpointIds" in data:
        import aws_sdk_global_accelerator.types.endpoint_ids

        out["endpoint_ids"] = (
            aws_sdk_global_accelerator.types.endpoint_ids.deserialize_aws_json_1_1(
                data["EndpointIds"]
            )
        )
    else:
        raise DeserializationError(
            "RemoveCustomRoutingEndpointsRequest.endpoint_ids required"
        )
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError(
            "RemoveCustomRoutingEndpointsRequest.endpoint_group_arn required"
        )
    return out

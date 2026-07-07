"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingEndpointDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class CustomRoutingEndpointDescription(TypedDict, closed=True):
    endpoint_id: NotRequired[
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>An ID for the endpoint. For custom routing accelerators, this is the virtual private cloud (VPC) subnet ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingEndpointDescription) -> dict:
    out: dict = {}
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRoutingEndpointDescription:
    out: CustomRoutingEndpointDescription = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    return out

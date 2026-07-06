"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_boolean
    import aws_sdk_global_accelerator.types.generic_string


class EndpointIdentifier(TypedDict, closed=True):
    endpoint_id: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>An ID for the endpoint. If the endpoint is a Network Load Balancer or Application Load Balancer, this is the Amazon Resource Name (ARN) of the resource. If the endpoint is an Elastic IP address, this is the Elastic IP address allocation ID. For Amazon EC2 instances, this is the EC2 instance ID. </p> <p>An Application Load Balancer can be either internal or internet-facing.</p>"""
    client_ip_preservation_enabled: NotRequired[
        "aws_sdk_global_accelerator.types.generic_boolean.GenericBoolean"
    ]
    """<p>Indicates whether client IP address preservation is enabled for an endpoint. The value is true or false. </p> <p>If the value is set to true, the client's IP address is preserved in the <code>X-Forwarded-For</code> request header as traffic travels to applications on the endpoint fronted by the accelerator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointIdentifier) -> dict:
    out: dict = {}
    out["EndpointId"] = value["endpoint_id"]
    if "client_ip_preservation_enabled" in value:
        out["ClientIPPreservationEnabled"] = value["client_ip_preservation_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointIdentifier:
    out: EndpointIdentifier = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    else:
        raise DeserializationError("EndpointIdentifier.endpoint_id required")
    if "ClientIPPreservationEnabled" in data:
        out["client_ip_preservation_enabled"] = data["ClientIPPreservationEnabled"]
    return out

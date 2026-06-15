"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Resource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.generic_string


class Resource(TypedDict):
    endpoint_id: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The endpoint ID for the endpoint that is specified as a Amazon Web Services resource. </p> <p>An endpoint ID for the cross-account feature is the ARN of an Amazon Web Services resource, such as a Network Load Balancer, that Global Accelerator supports as an endpoint for an accelerator.</p>"""
    cidr: NotRequired["aws_sdk_global_accelerator.types.generic_string.GenericString"]
    r"""<p>An IP address range, in CIDR format, that is specified as resource. The address must be provisioned and advertised in Global Accelerator by following the bring your own IP address (BYOIP) process for Global Accelerator</p> <p> For more information, see <a href=\"https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html\">Bring your own IP addresses (BYOIP)</a> in the Global Accelerator Developer Guide.</p>"""
    region: NotRequired["aws_sdk_global_accelerator.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Region where a shared endpoint resource is located.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    out["EndpointId"] = value.get("endpoint_id", "")
    if "cidr" in value:
        out["Cidr"] = value["cidr"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    else:
        out["endpoint_id"] = ""
    if "Cidr" in data:
        out["cidr"] = data["Cidr"]
    if "Region" in data:
        out["region"] = data["Region"]
    return out

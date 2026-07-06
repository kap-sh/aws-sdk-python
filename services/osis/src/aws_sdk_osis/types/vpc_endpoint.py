"""Generated from Smithy shape ``com.amazonaws.osis#VpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.string
    import aws_sdk_osis.types.vpc_options


class VpcEndpoint(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The unique identifier of the endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The ID for your VPC. Amazon Web Services PrivateLink generates this value when you create a VPC.</p>"""
    vpc_options: NotRequired["aws_sdk_osis.types.vpc_options.VpcOptions"]
    """<p>Information about the VPC, including associated subnets and security groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcEndpoint) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_options" in value:
        import aws_sdk_osis.types.vpc_options

        out["VpcOptions"] = aws_sdk_osis.types.vpc_options.serialize_json(
            value["vpc_options"]
        )
    return out


def deserialize_json(data: dict) -> VpcEndpoint:
    out: VpcEndpoint = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcOptions" in data:
        import aws_sdk_osis.types.vpc_options

        out["vpc_options"] = aws_sdk_osis.types.vpc_options.deserialize_json(
            data["VpcOptions"]
        )
    return out

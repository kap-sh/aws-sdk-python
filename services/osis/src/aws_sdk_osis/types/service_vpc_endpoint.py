"""Generated from Smithy shape ``com.amazonaws.osis#ServiceVpcEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.string
    import aws_sdk_osis.types.vpc_endpoint_service_name


class ServiceVpcEndpoint(TypedDict, closed=True):
    service_name: NotRequired[
        "aws_sdk_osis.types.vpc_endpoint_service_name.VpcEndpointServiceName"
    ]
    """<p>The name of the service for which a VPC endpoint was created.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The unique identifier of the VPC endpoint that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceVpcEndpoint) -> dict:
    out: dict = {}
    if "service_name" in value:
        import aws_sdk_osis.types.vpc_endpoint_service_name

        out["ServiceName"] = (
            aws_sdk_osis.types.vpc_endpoint_service_name.serialize_json(
                value["service_name"]
            )
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_json(data: dict) -> ServiceVpcEndpoint:
    out: ServiceVpcEndpoint = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        import aws_sdk_osis.types.vpc_endpoint_service_name

        out["service_name"] = (
            aws_sdk_osis.types.vpc_endpoint_service_name.deserialize_json(
                data["ServiceName"]
            )
        )
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out

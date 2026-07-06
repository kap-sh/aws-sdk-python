"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreateVpcEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.client_token
    import aws_sdk_elasticsearch_service.types.domain_arn
    import aws_sdk_elasticsearch_service.types.vpc_options


class CreateVpcEndpointRequest(TypedDict, closed=True):
    domain_arn: "aws_sdk_elasticsearch_service.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) of the domain to grant access to.</p>"""
    vpc_options: "aws_sdk_elasticsearch_service.types.vpc_options.VPCOptions"
    """<p>Options to specify the subnets and security groups for the endpoint.</p>"""
    client_token: NotRequired[
        "aws_sdk_elasticsearch_service.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["DomainArn"] = value["domain_arn"]
    import aws_sdk_elasticsearch_service.types.vpc_options

    out["VpcOptions"] = aws_sdk_elasticsearch_service.types.vpc_options.serialize_json(
        value["vpc_options"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateVpcEndpointRequest:
    out: CreateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    else:
        raise DeserializationError("CreateVpcEndpointRequest.domain_arn required")
    if "VpcOptions" in data:
        import aws_sdk_elasticsearch_service.types.vpc_options

        out["vpc_options"] = (
            aws_sdk_elasticsearch_service.types.vpc_options.deserialize_json(
                data["VpcOptions"]
            )
        )
    else:
        raise DeserializationError("CreateVpcEndpointRequest.vpc_options required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class DeleteResolverEndpointRequest(TypedDict):
    resolver_endpoint_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverEndpointRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverEndpointRequest:
    out: DeleteResolverEndpointRequest = {}  # type: ignore[typeddict-item]
    if "ResolverEndpointId" in data:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        raise DeserializationError(
            "DeleteResolverEndpointRequest.resolver_endpoint_id required"
        )
    return out

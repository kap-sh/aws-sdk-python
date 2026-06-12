"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverQueryLogConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class DeleteResolverQueryLogConfigRequest(TypedDict):
    resolver_query_log_config_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the query logging configuration that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverQueryLogConfigRequest) -> dict:
    out: dict = {}
    out["ResolverQueryLogConfigId"] = value["resolver_query_log_config_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverQueryLogConfigRequest:
    out: DeleteResolverQueryLogConfigRequest = {}  # type: ignore[typeddict-item]
    if "ResolverQueryLogConfigId" in data:
        out["resolver_query_log_config_id"] = data["ResolverQueryLogConfigId"]
    else:
        raise DeserializationError(
            "DeleteResolverQueryLogConfigRequest.resolver_query_log_config_id required"
        )
    return out

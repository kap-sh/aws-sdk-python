"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteResolverRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class DeleteResolverRuleRequest(TypedDict):
    resolver_rule_id: "aws_sdk_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver rule that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteResolverRuleRequest) -> dict:
    out: dict = {}
    out["ResolverRuleId"] = value["resolver_rule_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteResolverRuleRequest:
    out: DeleteResolverRuleRequest = {}  # type: ignore[typeddict-item]
    if "ResolverRuleId" in data:
        out["resolver_rule_id"] = data["ResolverRuleId"]
    else:
        raise DeserializationError(
            "DeleteResolverRuleRequest.resolver_rule_id required"
        )
    return out

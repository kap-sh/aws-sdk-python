"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverRulePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.arn


class GetResolverRulePolicyRequest(TypedDict):
    arn: "aws_sdk_route53resolver.types.arn.Arn"
    """<p>The ID of the Resolver rule that you want to get the Resolver rule policy for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverRulePolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverRulePolicyRequest:
    out: GetResolverRulePolicyRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetResolverRulePolicyRequest.arn required")
    return out

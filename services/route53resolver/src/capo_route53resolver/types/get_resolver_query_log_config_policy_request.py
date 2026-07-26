"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetResolverQueryLogConfigPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.arn


class GetResolverQueryLogConfigPolicyRequest(TypedDict, closed=True):
    arn: "capo_route53resolver.types.arn.Arn"
    """<p>The ARN of the query logging configuration that you want to get the query logging policy for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResolverQueryLogConfigPolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResolverQueryLogConfigPolicyRequest:
    out: GetResolverQueryLogConfigPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "GetResolverQueryLogConfigPolicyRequest.arn required"
        )
    return out

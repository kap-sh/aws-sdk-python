"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutResolverQueryLogConfigPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.boolean


class PutResolverQueryLogConfigPolicyResponse(TypedDict, closed=True):
    return_value: "capo_route53resolver.types.boolean.Boolean"
    """<p>Whether the <code>PutResolverQueryLogConfigPolicy</code> request was successful.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResolverQueryLogConfigPolicyResponse) -> dict:
    out: dict = {}
    out["ReturnValue"] = value.get("return_value", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResolverQueryLogConfigPolicyResponse:
    out: PutResolverQueryLogConfigPolicyResponse = {}  # type: ignore[typeddict-item]
    if "ReturnValue" in data:
        out["return_value"] = data["ReturnValue"]
    else:
        out["return_value"] = False
    return out

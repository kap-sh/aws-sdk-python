"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServicePolicyDisassociatedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn


class ServicePolicyDisassociatedMetadata(TypedDict, closed=True):
    policy_name: NotRequired["str"]
    """<p>The name of the disassociated policy.</p>"""
    policy_arn: NotRequired["aws_sdk_resiliencehubv2.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ServicePolicyDisassociatedMetadata) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_arn" in value:
        out["policyArn"] = value["policy_arn"]
    return out


def deserialize_json(data: dict) -> ServicePolicyDisassociatedMetadata:
    out: ServicePolicyDisassociatedMetadata = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyArn" in data:
        out["policy_arn"] = data["policyArn"]
    return out

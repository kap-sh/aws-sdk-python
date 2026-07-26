"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.resource_arn
    import capo_marketplace_catalog.types.resource_policy_json


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_marketplace_catalog.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the entity resource you want to associate with a resource policy.</p>"""
    policy: "capo_marketplace_catalog.types.resource_policy_json.ResourcePolicyJson"
    """<p>The policy document to set; formatted in JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out

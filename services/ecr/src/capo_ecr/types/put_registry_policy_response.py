"""Generated from Smithy shape ``com.amazonaws.ecr#PutRegistryPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.registry_id
    import capo_ecr.types.registry_policy_text


class PutRegistryPolicyResponse(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    policy_text: NotRequired["capo_ecr.types.registry_policy_text.RegistryPolicyText"]
    """<p>The JSON policy text for your registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRegistryPolicyResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "policy_text" in value:
        out["policyText"] = value["policy_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRegistryPolicyResponse:
    out: PutRegistryPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("policyText") is not None:
        out["policy_text"] = data["policyText"]
    return out

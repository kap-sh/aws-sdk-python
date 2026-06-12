"""Generated from Smithy shape ``com.amazonaws.iot#PolicyVersionIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.policy_name
    import aws_sdk_iot.types.policy_version_id


class PolicyVersionIdentifier(TypedDict):
    policy_name: NotRequired["aws_sdk_iot.types.policy_name.PolicyName"]
    """<p>The name of the policy.</p>"""
    policy_version_id: NotRequired[
        "aws_sdk_iot.types.policy_version_id.PolicyVersionId"
    ]
    """<p>The ID of the version of the policy associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyVersionIdentifier) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "policy_version_id" in value:
        out["policyVersionId"] = value["policy_version_id"]
    return out


def deserialize_json(data: dict) -> PolicyVersionIdentifier:
    out: PolicyVersionIdentifier = {}  # type: ignore[typeddict-item]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "policyVersionId" in data:
        out["policy_version_id"] = data["policyVersionId"]
    return out

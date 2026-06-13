"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PutResourcePolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.policy_id


class PutResourcePolicyOutput(TypedDict):
    policy_id: "aws_sdk_ssm_incidents.types.policy_id.PolicyId"
    """<p>The ID of the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyOutput) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyOutput:
    out: PutResourcePolicyOutput = {}  # type: ignore[typeddict-item]
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("PutResourcePolicyOutput.policy_id required")
    return out

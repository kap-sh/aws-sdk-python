"""Generated from Smithy shape ``com.amazonaws.dsql#PutClusterPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.policy_version


class PutClusterPolicyOutput(TypedDict, closed=True):
    policy_version: "aws_sdk_dsql.types.policy_version.PolicyVersion"
    """<p>The version of the policy after it has been updated or created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutClusterPolicyOutput) -> dict:
    out: dict = {}
    out["policyVersion"] = value["policy_version"]
    return out


def deserialize_json(data: dict) -> PutClusterPolicyOutput:
    out: PutClusterPolicyOutput = {}  # type: ignore[typeddict-item]
    if "policyVersion" in data:
        out["policy_version"] = data["policyVersion"]
    else:
        raise DeserializationError("PutClusterPolicyOutput.policy_version required")
    return out

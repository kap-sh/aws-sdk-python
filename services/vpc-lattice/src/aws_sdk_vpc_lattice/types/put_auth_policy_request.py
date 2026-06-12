"""Generated from Smithy shape ``com.amazonaws.vpclattice#PutAuthPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.auth_policy_string
    import aws_sdk_vpc_lattice.types.resource_identifier


class PutAuthPolicyRequest(TypedDict):
    resource_identifier: (
        "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The ID or ARN of the service network or service for which the policy is created.</p>"""
    policy: "aws_sdk_vpc_lattice.types.auth_policy_string.AuthPolicyString"
    """<p>The auth policy. The policy string in JSON must not contain newlines or blank lines.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAuthPolicyRequest) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutAuthPolicyRequest:
    out: PutAuthPolicyRequest = {}  # type: ignore[typeddict-item]
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutAuthPolicyRequest.policy required")
    return out

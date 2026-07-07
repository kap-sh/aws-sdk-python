"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ResourcePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.policy
    import aws_sdk_ssm_incidents.types.policy_id


class ResourcePolicy(TypedDict, closed=True):
    policy_document: "aws_sdk_ssm_incidents.types.policy.Policy"
    """<p>The JSON blob that describes the policy.</p>"""
    policy_id: "aws_sdk_ssm_incidents.types.policy_id.PolicyId"
    """<p>The ID of the resource policy.</p>"""
    ram_resource_share_region: "str"
    """<p>The Amazon Web Services Region that policy allows resources to be used in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePolicy) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    out["policyId"] = value["policy_id"]
    out["ramResourceShareRegion"] = value["ram_resource_share_region"]
    return out


def deserialize_json(data: dict) -> ResourcePolicy:
    out: ResourcePolicy = {}  # type: ignore[typeddict-item]
    if "policyDocument" in data:
        out["policy_document"] = data["policyDocument"]
    else:
        raise DeserializationError("ResourcePolicy.policy_document required")
    if "policyId" in data:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("ResourcePolicy.policy_id required")
    if "ramResourceShareRegion" in data:
        out["ram_resource_share_region"] = data["ramResourceShareRegion"]
    else:
        raise DeserializationError("ResourcePolicy.ram_resource_share_region required")
    return out

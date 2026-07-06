"""Generated from Smithy shape ``com.amazonaws.ssmincidents#PutResourcePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.policy


class PutResourcePolicyInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan to add the resource policy to.</p>"""
    policy: "aws_sdk_ssm_incidents.types.policy.Policy"
    """<p>Details of the resource policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyInput:
    out: PutResourcePolicyInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyInput.resource_arn required")
    if "policy" in data:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutResourcePolicyInput.policy required")
    return out

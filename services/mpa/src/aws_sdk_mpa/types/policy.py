"""Generated from Smithy shape ``com.amazonaws.mpa#Policy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mpa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mpa.types.policy_name
    import aws_sdk_mpa.types.policy_type
    import aws_sdk_mpa.types.policy_version_id
    import aws_sdk_mpa.types.unqualified_policy_arn


class Policy(TypedDict):
    arn: "aws_sdk_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""
    default_version: "aws_sdk_mpa.types.policy_version_id.PolicyVersionId"
    """<p>Determines if the specified policy is the default for the team.</p>"""
    policy_type: "aws_sdk_mpa.types.policy_type.PolicyType"
    """<p>The type of policy.</p>"""
    name: "aws_sdk_mpa.types.policy_name.PolicyName"
    """<p>Name of the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["DefaultVersion"] = value["default_version"]
    import aws_sdk_mpa.types.policy_type

    out["PolicyType"] = aws_sdk_mpa.types.policy_type.serialize_json(
        value["policy_type"]
    )
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Policy:
    out: Policy = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Policy.arn required")
    if "DefaultVersion" in data:
        out["default_version"] = data["DefaultVersion"]
    else:
        raise DeserializationError("Policy.default_version required")
    if "PolicyType" in data:
        import aws_sdk_mpa.types.policy_type

        out["policy_type"] = aws_sdk_mpa.types.policy_type.deserialize_json(
            data["PolicyType"]
        )
    else:
        raise DeserializationError("Policy.policy_type required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Policy.name required")
    return out

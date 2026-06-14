"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#StaticPolicyDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.policy_statement
    import aws_sdk_verifiedpermissions.types.static_policy_description


class StaticPolicyDefinition(TypedDict):
    description: NotRequired[
        "aws_sdk_verifiedpermissions.types.static_policy_description.StaticPolicyDescription"
    ]
    """<p>The description of the static policy.</p>"""
    statement: "aws_sdk_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>The policy content of the static policy, written in the Cedar policy language.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticPolicyDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StaticPolicyDefinition:
    out: StaticPolicyDefinition = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "statement" in data:
        out["statement"] = data["statement"]
    else:
        raise DeserializationError("StaticPolicyDefinition.statement required")
    return out

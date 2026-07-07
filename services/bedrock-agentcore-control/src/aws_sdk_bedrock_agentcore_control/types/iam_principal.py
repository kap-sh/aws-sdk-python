"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IamPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.iam_principal_arn
    import aws_sdk_bedrock_agentcore_control.types.principal_match_operator


class IamPrincipal(TypedDict, closed=True):
    arn: "aws_sdk_bedrock_agentcore_control.types.iam_principal_arn.IamPrincipalArn"
    """<p>The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the <code>StringLike</code> operator.</p>"""
    operator: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.principal_match_operator.PrincipalMatchOperator"
    ]
    """<p>The match operator. <code>StringEquals</code> requires an exact match. <code>StringLike</code> supports wildcard patterns using <code>*</code> and <code>?</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPrincipal) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "operator" in value:
        import aws_sdk_bedrock_agentcore_control.types.principal_match_operator

        out["operator"] = (
            aws_sdk_bedrock_agentcore_control.types.principal_match_operator.serialize_json(
                value["operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> IamPrincipal:
    out: IamPrincipal = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IamPrincipal.arn required")
    if "operator" in data:
        import aws_sdk_bedrock_agentcore_control.types.principal_match_operator

        out["operator"] = (
            aws_sdk_bedrock_agentcore_control.types.principal_match_operator.deserialize_json(
                data["operator"]
            )
        )
    return out

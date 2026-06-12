"""Generated from Smithy shape ``com.amazonaws.connect#CreateRuleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.rule_id


class CreateRuleResponse(TypedDict):
    rule_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    rule_id: "aws_sdk_connect.types.rule_id.RuleId"
    """<p>A unique identifier for the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleResponse) -> dict:
    out: dict = {}
    out["RuleArn"] = value["rule_arn"]
    out["RuleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> CreateRuleResponse:
    out: CreateRuleResponse = {}  # type: ignore[typeddict-item]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    else:
        raise DeserializationError("CreateRuleResponse.rule_arn required")
    if "RuleId" in data:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("CreateRuleResponse.rule_id required")
    return out

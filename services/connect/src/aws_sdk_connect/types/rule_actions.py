"""Generated from Smithy shape ``com.amazonaws.connect#RuleActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.rule_action

RuleActions: TypeAlias = list["aws_sdk_connect.types.rule_action.RuleAction"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleActions) -> list:
    import aws_sdk_connect.types.rule_action

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.rule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleActions:
    import aws_sdk_connect.types.rule_action

    out: RuleActions = []
    for item in data:
        out.append(aws_sdk_connect.types.rule_action.deserialize_json(item))
    return out

"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedRuleArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_notifications.types.managed_rule_arn

ManagedRuleArns: TypeAlias = list[
    "aws_sdk_notifications.types.managed_rule_arn.ManagedRuleArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedRuleArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ManagedRuleArns:
    return list(data)

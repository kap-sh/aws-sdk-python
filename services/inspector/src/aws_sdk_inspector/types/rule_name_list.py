"""Generated from Smithy shape ``com.amazonaws.inspector#RuleNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.rule_name

RuleNameList: TypeAlias = list["aws_sdk_inspector.types.rule_name.RuleName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RuleNameList:
    return list(data)

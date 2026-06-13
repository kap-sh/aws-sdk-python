"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.rule_result

RuleResultList: TypeAlias = list["aws_sdk_ssm_sap.types.rule_result.RuleResult"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleResultList) -> list:
    import aws_sdk_ssm_sap.types.rule_result

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.rule_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleResultList:
    import aws_sdk_ssm_sap.types.rule_result

    out: RuleResultList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.rule_result.deserialize_json(item))
    return out

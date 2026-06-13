"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.rule

RuleList: TypeAlias = list["aws_sdk_entityresolution.types.rule.Rule"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleList) -> list:
    import aws_sdk_entityresolution.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleList:
    import aws_sdk_entityresolution.types.rule

    out: RuleList = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.rule.deserialize_json(item))
    return out

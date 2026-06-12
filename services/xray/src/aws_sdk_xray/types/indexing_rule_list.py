"""Generated from Smithy shape ``com.amazonaws.xray#IndexingRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.indexing_rule

IndexingRuleList: TypeAlias = list["aws_sdk_xray.types.indexing_rule.IndexingRule"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexingRuleList) -> list:
    import aws_sdk_xray.types.indexing_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.indexing_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> IndexingRuleList:
    import aws_sdk_xray.types.indexing_rule

    out: IndexingRuleList = []
    for item in data:
        out.append(aws_sdk_xray.types.indexing_rule.deserialize_json(item))
    return out

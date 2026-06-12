"""Generated from Smithy shape ``com.amazonaws.glacier#DataRetrievalRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glacier.types.data_retrieval_rule

DataRetrievalRulesList: TypeAlias = list[
    "aws_sdk_glacier.types.data_retrieval_rule.DataRetrievalRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataRetrievalRulesList) -> list:
    import aws_sdk_glacier.types.data_retrieval_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_glacier.types.data_retrieval_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataRetrievalRulesList:
    import aws_sdk_glacier.types.data_retrieval_rule

    out: DataRetrievalRulesList = []
    for item in data:
        out.append(aws_sdk_glacier.types.data_retrieval_rule.deserialize_json(item))
    return out

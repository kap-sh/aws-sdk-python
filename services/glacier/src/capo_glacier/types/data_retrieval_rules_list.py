"""Generated from Smithy shape ``com.amazonaws.glacier#DataRetrievalRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glacier.types.data_retrieval_rule

DataRetrievalRulesList: TypeAlias = list[
    "capo_glacier.types.data_retrieval_rule.DataRetrievalRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataRetrievalRulesList) -> list:
    import capo_glacier.types.data_retrieval_rule

    out: list = []
    for item in value:
        out.append(capo_glacier.types.data_retrieval_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataRetrievalRulesList:
    import capo_glacier.types.data_retrieval_rule

    out: DataRetrievalRulesList = []
    for item in data:
        out.append(capo_glacier.types.data_retrieval_rule.deserialize_json(item))
    return out

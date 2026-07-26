"""Generated from Smithy shape ``com.amazonaws.wisdom#AssistantAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.assistant_association_summary

AssistantAssociationSummaryList: TypeAlias = list[
    "capo_wisdom.types.assistant_association_summary.AssistantAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationSummaryList) -> list:
    import capo_wisdom.types.assistant_association_summary

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.assistant_association_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssistantAssociationSummaryList:
    import capo_wisdom.types.assistant_association_summary

    out: AssistantAssociationSummaryList = []
    for item in data:
        out.append(
            capo_wisdom.types.assistant_association_summary.deserialize_json(item)
        )
    return out

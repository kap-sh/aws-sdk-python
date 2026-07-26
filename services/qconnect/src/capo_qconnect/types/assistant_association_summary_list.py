"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.assistant_association_summary

AssistantAssociationSummaryList: TypeAlias = list[
    "capo_qconnect.types.assistant_association_summary.AssistantAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationSummaryList) -> list:
    import capo_qconnect.types.assistant_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.assistant_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssistantAssociationSummaryList:
    import capo_qconnect.types.assistant_association_summary

    out: AssistantAssociationSummaryList = []
    for item in data:
        out.append(
            capo_qconnect.types.assistant_association_summary.deserialize_json(item)
        )
    return out

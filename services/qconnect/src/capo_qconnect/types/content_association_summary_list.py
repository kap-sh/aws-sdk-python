"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.content_association_summary

ContentAssociationSummaryList: TypeAlias = list[
    "capo_qconnect.types.content_association_summary.ContentAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentAssociationSummaryList) -> list:
    import capo_qconnect.types.content_association_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.content_association_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentAssociationSummaryList:
    import capo_qconnect.types.content_association_summary

    out: ContentAssociationSummaryList = []
    for item in data:
        out.append(
            capo_qconnect.types.content_association_summary.deserialize_json(item)
        )
    return out

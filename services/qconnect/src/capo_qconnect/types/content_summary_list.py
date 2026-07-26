"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.content_summary

ContentSummaryList: TypeAlias = list[
    "capo_qconnect.types.content_summary.ContentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentSummaryList) -> list:
    import capo_qconnect.types.content_summary

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.content_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContentSummaryList:
    import capo_qconnect.types.content_summary

    out: ContentSummaryList = []
    for item in data:
        out.append(capo_qconnect.types.content_summary.deserialize_json(item))
    return out

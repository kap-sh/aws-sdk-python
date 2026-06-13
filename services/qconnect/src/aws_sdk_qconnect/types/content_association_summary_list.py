"""Generated from Smithy shape ``com.amazonaws.qconnect#ContentAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_association_summary

ContentAssociationSummaryList: TypeAlias = list[
    "aws_sdk_qconnect.types.content_association_summary.ContentAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContentAssociationSummaryList) -> list:
    import aws_sdk_qconnect.types.content_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_qconnect.types.content_association_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContentAssociationSummaryList:
    import aws_sdk_qconnect.types.content_association_summary

    out: ContentAssociationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_qconnect.types.content_association_summary.deserialize_json(item)
        )
    return out

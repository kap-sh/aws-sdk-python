"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessPreviewsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.access_preview_summary

AccessPreviewsList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.access_preview_summary.AccessPreviewSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPreviewsList) -> list:
    import aws_sdk_accessanalyzer.types.access_preview_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.access_preview_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessPreviewsList:
    import aws_sdk_accessanalyzer.types.access_preview_summary

    out: AccessPreviewsList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.access_preview_summary.deserialize_json(item)
        )
    return out

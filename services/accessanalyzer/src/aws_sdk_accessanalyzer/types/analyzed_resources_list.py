"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzedResourcesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzed_resource_summary

AnalyzedResourcesList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.analyzed_resource_summary.AnalyzedResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzedResourcesList) -> list:
    import aws_sdk_accessanalyzer.types.analyzed_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_accessanalyzer.types.analyzed_resource_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AnalyzedResourcesList:
    import aws_sdk_accessanalyzer.types.analyzed_resource_summary

    out: AnalyzedResourcesList = []
    for item in data:
        out.append(
            aws_sdk_accessanalyzer.types.analyzed_resource_summary.deserialize_json(
                item
            )
        )
    return out

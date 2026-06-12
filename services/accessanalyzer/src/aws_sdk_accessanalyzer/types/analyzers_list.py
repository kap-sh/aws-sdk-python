"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_summary

AnalyzersList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.analyzer_summary.AnalyzerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzersList) -> list:
    import aws_sdk_accessanalyzer.types.analyzer_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.analyzer_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalyzersList:
    import aws_sdk_accessanalyzer.types.analyzer_summary

    out: AnalyzersList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.analyzer_summary.deserialize_json(item))
    return out

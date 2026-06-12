"""Generated from Smithy shape ``com.amazonaws.forecast#ExplainabilityExports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.explainability_export_summary

ExplainabilityExports: TypeAlias = list[
    "aws_sdk_forecast.types.explainability_export_summary.ExplainabilityExportSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainabilityExports) -> list:
    import aws_sdk_forecast.types.explainability_export_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.explainability_export_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExplainabilityExports:
    import aws_sdk_forecast.types.explainability_export_summary

    out: ExplainabilityExports = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.explainability_export_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

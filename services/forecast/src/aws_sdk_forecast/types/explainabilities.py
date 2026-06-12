"""Generated from Smithy shape ``com.amazonaws.forecast#Explainabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.explainability_summary

Explainabilities: TypeAlias = list[
    "aws_sdk_forecast.types.explainability_summary.ExplainabilitySummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Explainabilities) -> list:
    import aws_sdk_forecast.types.explainability_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.explainability_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Explainabilities:
    import aws_sdk_forecast.types.explainability_summary

    out: Explainabilities = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.explainability_summary.deserialize_aws_json_1_1(item)
        )
    return out

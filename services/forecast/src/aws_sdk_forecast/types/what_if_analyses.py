"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfAnalyses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_forecast.types.what_if_analysis_summary

WhatIfAnalyses: TypeAlias = list[
    "aws_sdk_forecast.types.what_if_analysis_summary.WhatIfAnalysisSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfAnalyses) -> list:
    import aws_sdk_forecast.types.what_if_analysis_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_forecast.types.what_if_analysis_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WhatIfAnalyses:
    import aws_sdk_forecast.types.what_if_analysis_summary

    out: WhatIfAnalyses = []
    for item in data:
        out.append(
            aws_sdk_forecast.types.what_if_analysis_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.forecast#WhatIfAnalyses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.what_if_analysis_summary

WhatIfAnalyses: TypeAlias = list[
    "capo_forecast.types.what_if_analysis_summary.WhatIfAnalysisSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WhatIfAnalyses) -> list:
    import capo_forecast.types.what_if_analysis_summary

    out: list = []
    for item in value:
        out.append(
            capo_forecast.types.what_if_analysis_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> WhatIfAnalyses:
    import capo_forecast.types.what_if_analysis_summary

    out: WhatIfAnalyses = []
    for item in data:
        out.append(
            capo_forecast.types.what_if_analysis_summary.deserialize_aws_json_1_1(item)
        )
    return out

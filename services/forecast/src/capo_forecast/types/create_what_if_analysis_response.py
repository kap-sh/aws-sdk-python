"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn


class CreateWhatIfAnalysisResponse(TypedDict, closed=True):
    what_if_analysis_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the what-if analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWhatIfAnalysisResponse) -> dict:
    out: dict = {}
    if "what_if_analysis_arn" in value:
        out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWhatIfAnalysisResponse:
    out: CreateWhatIfAnalysisResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfAnalysisArn" in data:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    return out

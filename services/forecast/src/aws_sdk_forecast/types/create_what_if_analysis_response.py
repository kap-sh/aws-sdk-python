"""Generated from Smithy shape ``com.amazonaws.forecast#CreateWhatIfAnalysisResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class CreateWhatIfAnalysisResponse(TypedDict):
    what_if_analysis_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
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

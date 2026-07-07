"""Generated from Smithy shape ``com.amazonaws.forecast#DeleteWhatIfAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn


class DeleteWhatIfAnalysisRequest(TypedDict, closed=True):
    what_if_analysis_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the what-if analysis that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWhatIfAnalysisRequest) -> dict:
    out: dict = {}
    out["WhatIfAnalysisArn"] = value["what_if_analysis_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWhatIfAnalysisRequest:
    out: DeleteWhatIfAnalysisRequest = {}  # type: ignore[typeddict-item]
    if "WhatIfAnalysisArn" in data:
        out["what_if_analysis_arn"] = data["WhatIfAnalysisArn"]
    else:
        raise DeserializationError(
            "DeleteWhatIfAnalysisRequest.what_if_analysis_arn required"
        )
    return out

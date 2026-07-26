"""Generated from Smithy shape ``com.amazonaws.forecast#ListWhatIfAnalysesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.next_token
    import capo_forecast.types.what_if_analyses


class ListWhatIfAnalysesResponse(TypedDict, closed=True):
    what_if_analyses: NotRequired["capo_forecast.types.what_if_analyses.WhatIfAnalyses"]
    """<p>An array of <code>WhatIfAnalysisSummary</code> objects that describe the matched analyses.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWhatIfAnalysesResponse) -> dict:
    out: dict = {}
    if "what_if_analyses" in value:
        import capo_forecast.types.what_if_analyses

        out["WhatIfAnalyses"] = (
            capo_forecast.types.what_if_analyses.serialize_aws_json_1_1(
                value["what_if_analyses"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWhatIfAnalysesResponse:
    out: ListWhatIfAnalysesResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfAnalyses" in data:
        import capo_forecast.types.what_if_analyses

        out["what_if_analyses"] = (
            capo_forecast.types.what_if_analyses.deserialize_aws_json_1_1(
                data["WhatIfAnalyses"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

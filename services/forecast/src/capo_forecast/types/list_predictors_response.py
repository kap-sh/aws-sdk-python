"""Generated from Smithy shape ``com.amazonaws.forecast#ListPredictorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.next_token
    import capo_forecast.types.predictors


class ListPredictorsResponse(TypedDict, closed=True):
    predictors: NotRequired["capo_forecast.types.predictors.Predictors"]
    """<p>An array of objects that summarize each predictor's properties.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPredictorsResponse) -> dict:
    out: dict = {}
    if "predictors" in value:
        import capo_forecast.types.predictors

        out["Predictors"] = capo_forecast.types.predictors.serialize_aws_json_1_1(
            value["predictors"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPredictorsResponse:
    out: ListPredictorsResponse = {}  # type: ignore[typeddict-item]
    if "Predictors" in data:
        import capo_forecast.types.predictors

        out["predictors"] = capo_forecast.types.predictors.deserialize_aws_json_1_1(
            data["Predictors"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.forecast#ListExplainabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.explainabilities
    import capo_forecast.types.next_token


class ListExplainabilitiesResponse(TypedDict, closed=True):
    explainabilities: NotRequired[
        "capo_forecast.types.explainabilities.Explainabilities"
    ]
    """<p>An array of objects that summarize the properties of each Explainability resource.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>Returns this token if the response is truncated. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExplainabilitiesResponse) -> dict:
    out: dict = {}
    if "explainabilities" in value:
        import capo_forecast.types.explainabilities

        out["Explainabilities"] = (
            capo_forecast.types.explainabilities.serialize_aws_json_1_1(
                value["explainabilities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExplainabilitiesResponse:
    out: ListExplainabilitiesResponse = {}  # type: ignore[typeddict-item]
    if "Explainabilities" in data:
        import capo_forecast.types.explainabilities

        out["explainabilities"] = (
            capo_forecast.types.explainabilities.deserialize_aws_json_1_1(
                data["Explainabilities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

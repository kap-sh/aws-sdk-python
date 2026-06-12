"""Generated from Smithy shape ``com.amazonaws.forecast#ListDatasetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.datasets
    import aws_sdk_forecast.types.next_token


class ListDatasetsResponse(TypedDict):
    datasets: NotRequired["aws_sdk_forecast.types.datasets.Datasets"]
    """<p>An array of objects that summarize each dataset's properties.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetsResponse) -> dict:
    out: dict = {}
    if "datasets" in value:
        import aws_sdk_forecast.types.datasets

        out["Datasets"] = aws_sdk_forecast.types.datasets.serialize_aws_json_1_1(
            value["datasets"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetsResponse:
    out: ListDatasetsResponse = {}  # type: ignore[typeddict-item]
    if "Datasets" in data:
        import aws_sdk_forecast.types.datasets

        out["datasets"] = aws_sdk_forecast.types.datasets.deserialize_aws_json_1_1(
            data["Datasets"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

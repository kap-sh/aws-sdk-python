"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTimeSeriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.next_token
    import aws_sdk_iotsitewise.types.time_series_summaries


class ListTimeSeriesResponse(TypedDict, closed=True):
    time_series_summaries: (
        "aws_sdk_iotsitewise.types.time_series_summaries.TimeSeriesSummaries"
    )
    """<p>One or more time series summaries to list.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTimeSeriesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.time_series_summaries

    out["TimeSeriesSummaries"] = (
        aws_sdk_iotsitewise.types.time_series_summaries.serialize_json(
            value["time_series_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTimeSeriesResponse:
    out: ListTimeSeriesResponse = {}  # type: ignore[typeddict-item]
    if "TimeSeriesSummaries" in data:
        import aws_sdk_iotsitewise.types.time_series_summaries

        out["time_series_summaries"] = (
            aws_sdk_iotsitewise.types.time_series_summaries.deserialize_json(
                data["TimeSeriesSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListTimeSeriesResponse.time_series_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out

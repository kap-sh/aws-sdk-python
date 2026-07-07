"""Generated from Smithy shape ``com.amazonaws.iot#GetStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.statistics


class GetStatisticsResponse(TypedDict, closed=True):
    statistics: NotRequired["aws_sdk_iot.types.statistics.Statistics"]
    """<p>The statistics returned by the Fleet Indexing service based on the query and aggregation field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStatisticsResponse) -> dict:
    out: dict = {}
    if "statistics" in value:
        import aws_sdk_iot.types.statistics

        out["statistics"] = aws_sdk_iot.types.statistics.serialize_json(
            value["statistics"]
        )
    return out


def deserialize_json(data: dict) -> GetStatisticsResponse:
    out: GetStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "statistics" in data:
        import aws_sdk_iot.types.statistics

        out["statistics"] = aws_sdk_iot.types.statistics.deserialize_json(
            data["statistics"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#ListSensorStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.next_token
    import capo_lookoutequipment.types.sensor_statistics_summaries


class ListSensorStatisticsResponse(TypedDict, closed=True):
    sensor_statistics_summaries: NotRequired[
        "capo_lookoutequipment.types.sensor_statistics_summaries.SensorStatisticsSummaries"
    ]
    """<p>Provides ingestion-based statistics regarding the specified sensor with respect to various validation types, such as whether data exists, the number and percentage of missing values, and the number and percentage of duplicate timestamps. </p>"""
    next_token: NotRequired["capo_lookoutequipment.types.next_token.NextToken"]
    """<p>An opaque pagination token indicating where to continue the listing of sensor statistics. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSensorStatisticsResponse) -> dict:
    out: dict = {}
    if "sensor_statistics_summaries" in value:
        import capo_lookoutequipment.types.sensor_statistics_summaries

        out["SensorStatisticsSummaries"] = (
            capo_lookoutequipment.types.sensor_statistics_summaries.serialize_aws_json_1_0(
                value["sensor_statistics_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSensorStatisticsResponse:
    out: ListSensorStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "SensorStatisticsSummaries" in data:
        import capo_lookoutequipment.types.sensor_statistics_summaries

        out["sensor_statistics_summaries"] = (
            capo_lookoutequipment.types.sensor_statistics_summaries.deserialize_aws_json_1_0(
                data["SensorStatisticsSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#StartSessionsStatisticsAggregationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.period
    import aws_sdk_deadline.types.sessions_statistics_resources
    import aws_sdk_deadline.types.timestamp
    import aws_sdk_deadline.types.timezone
    import aws_sdk_deadline.types.usage_group_by
    import aws_sdk_deadline.types.usage_statistics


class StartSessionsStatisticsAggregationRequest(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The identifier of the farm that contains queues or fleets to return statistics for.</p>"""
    resource_ids: "aws_sdk_deadline.types.sessions_statistics_resources.SessionsStatisticsResources"
    """<p>A list of fleet IDs or queue IDs to gather statistics for.</p>"""
    start_time: "aws_sdk_deadline.types.timestamp.Timestamp"
    """<p>The Linux timestamp of the date and time that the statistics start.</p>"""
    end_time: "aws_sdk_deadline.types.timestamp.Timestamp"
    """<p>The Linux timestamp of the date and time that the statistics end.</p>"""
    timezone: NotRequired["aws_sdk_deadline.types.timezone.Timezone"]
    r"""<p>The timezone to use for the statistics. Use UTC notation such as \"UTC+8.\"</p>"""
    period: NotRequired["aws_sdk_deadline.types.period.Period"]
    """<p>The period to aggregate the statistics.</p>"""
    group_by: "aws_sdk_deadline.types.usage_group_by.UsageGroupBy"
    """<p>The field to use to group the statistics.</p>"""
    statistics: "aws_sdk_deadline.types.usage_statistics.UsageStatistics"
    """<p>One to four statistics to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionsStatisticsAggregationRequest) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.sessions_statistics_resources

    out["resourceIds"] = (
        aws_sdk_deadline.types.sessions_statistics_resources.serialize_json(
            value["resource_ids"]
        )
    )
    import aws_sdk_deadline.types.timestamp

    out["startTime"] = aws_sdk_deadline.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_deadline.types.timestamp

    out["endTime"] = aws_sdk_deadline.types.timestamp.serialize_json(value["end_time"])
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "period" in value:
        import aws_sdk_deadline.types.period

        out["period"] = aws_sdk_deadline.types.period.serialize_json(value["period"])
    import aws_sdk_deadline.types.usage_group_by

    out["groupBy"] = aws_sdk_deadline.types.usage_group_by.serialize_json(
        value["group_by"]
    )
    import aws_sdk_deadline.types.usage_statistics

    out["statistics"] = aws_sdk_deadline.types.usage_statistics.serialize_json(
        value["statistics"]
    )
    return out


def deserialize_json(data: dict) -> StartSessionsStatisticsAggregationRequest:
    out: StartSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
    if "resourceIds" in data:
        import aws_sdk_deadline.types.sessions_statistics_resources

        out["resource_ids"] = (
            aws_sdk_deadline.types.sessions_statistics_resources.deserialize_json(
                data["resourceIds"]
            )
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.resource_ids required"
        )
    if "startTime" in data:
        import aws_sdk_deadline.types.timestamp

        out["start_time"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["startTime"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.start_time required"
        )
    if "endTime" in data:
        import aws_sdk_deadline.types.timestamp

        out["end_time"] = aws_sdk_deadline.types.timestamp.deserialize_json(
            data["endTime"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.end_time required"
        )
    if "timezone" in data:
        out["timezone"] = data["timezone"]
    if "period" in data:
        import aws_sdk_deadline.types.period

        out["period"] = aws_sdk_deadline.types.period.deserialize_json(data["period"])
    if "groupBy" in data:
        import aws_sdk_deadline.types.usage_group_by

        out["group_by"] = aws_sdk_deadline.types.usage_group_by.deserialize_json(
            data["groupBy"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.group_by required"
        )
    if "statistics" in data:
        import aws_sdk_deadline.types.usage_statistics

        out["statistics"] = aws_sdk_deadline.types.usage_statistics.deserialize_json(
            data["statistics"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.statistics required"
        )
    return out

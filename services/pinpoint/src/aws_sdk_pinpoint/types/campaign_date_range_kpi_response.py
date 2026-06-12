"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignDateRangeKpiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.__timestamp_iso8601
    import aws_sdk_pinpoint.types.base_kpi_result


class CampaignDateRangeKpiResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the metric applies to.</p>"""
    campaign_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the campaign that the metric applies to.</p>"""
    end_time: NotRequired[
        "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The last date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.</p>"""
    kpi_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, that the data was retrieved for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. For a list of possible values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.</p>"""
    kpi_result: NotRequired["aws_sdk_pinpoint.types.base_kpi_result.BaseKpiResult"]
    """<p>An array of objects that contains the results of the query. Each object contains the value for the metric and metadata about that value.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The string to use in a subsequent request to get the next page of results in a paginated response. This value is null for the Campaign Metrics resource because the resource returns all results in a single page.</p>"""
    start_time: NotRequired[
        "aws_sdk_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The first date and time of the date range that was used to filter the query results, in extended ISO 8601 format. The date range is inclusive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignDateRangeKpiResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "end_time" in value:
        import aws_sdk_pinpoint.types.__timestamp_iso8601

        out["EndTime"] = aws_sdk_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["end_time"]
        )
    if "kpi_name" in value:
        out["KpiName"] = value["kpi_name"]
    if "kpi_result" in value:
        import aws_sdk_pinpoint.types.base_kpi_result

        out["KpiResult"] = aws_sdk_pinpoint.types.base_kpi_result.serialize_json(
            value["kpi_result"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "start_time" in value:
        import aws_sdk_pinpoint.types.__timestamp_iso8601

        out["StartTime"] = aws_sdk_pinpoint.types.__timestamp_iso8601.serialize_json(
            value["start_time"]
        )
    return out


def deserialize_json(data: dict) -> CampaignDateRangeKpiResponse:
    out: CampaignDateRangeKpiResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "CampaignId" in data:
        out["campaign_id"] = data["CampaignId"]
    if "EndTime" in data:
        import aws_sdk_pinpoint.types.__timestamp_iso8601

        out["end_time"] = aws_sdk_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["EndTime"]
        )
    if "KpiName" in data:
        out["kpi_name"] = data["KpiName"]
    if "KpiResult" in data:
        import aws_sdk_pinpoint.types.base_kpi_result

        out["kpi_result"] = aws_sdk_pinpoint.types.base_kpi_result.deserialize_json(
            data["KpiResult"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "StartTime" in data:
        import aws_sdk_pinpoint.types.__timestamp_iso8601

        out["start_time"] = aws_sdk_pinpoint.types.__timestamp_iso8601.deserialize_json(
            data["StartTime"]
        )
    return out

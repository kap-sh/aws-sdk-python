"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageInsightsDataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.message_insights_export_max_results
    import aws_sdk_sesv2.types.message_insights_filters
    import aws_sdk_sesv2.types.timestamp


class MessageInsightsDataSource(TypedDict, closed=True):
    start_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the export interval as a timestamp. The start date is inclusive.</p>"""
    end_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the export interval as a timestamp. The end date is inclusive.</p>"""
    include: NotRequired[
        "aws_sdk_sesv2.types.message_insights_filters.MessageInsightsFilters"
    ]
    """<p>Filters for results to be included in the export file.</p>"""
    exclude: NotRequired[
        "aws_sdk_sesv2.types.message_insights_filters.MessageInsightsFilters"
    ]
    """<p>Filters for results to be excluded from the export file.</p>"""
    max_results: NotRequired[
        "aws_sdk_sesv2.types.message_insights_export_max_results.MessageInsightsExportMaxResults"
    ]
    """<p>The maximum number of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInsightsDataSource) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.timestamp

    out["StartDate"] = aws_sdk_sesv2.types.timestamp.serialize_json(value["start_date"])
    import aws_sdk_sesv2.types.timestamp

    out["EndDate"] = aws_sdk_sesv2.types.timestamp.serialize_json(value["end_date"])
    if "include" in value:
        import aws_sdk_sesv2.types.message_insights_filters

        out["Include"] = aws_sdk_sesv2.types.message_insights_filters.serialize_json(
            value["include"]
        )
    if "exclude" in value:
        import aws_sdk_sesv2.types.message_insights_filters

        out["Exclude"] = aws_sdk_sesv2.types.message_insights_filters.serialize_json(
            value["exclude"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> MessageInsightsDataSource:
    out: MessageInsightsDataSource = {}  # type: ignore[typeddict-item]
    if "StartDate" in data:
        import aws_sdk_sesv2.types.timestamp

        out["start_date"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        raise DeserializationError("MessageInsightsDataSource.start_date required")
    if "EndDate" in data:
        import aws_sdk_sesv2.types.timestamp

        out["end_date"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["EndDate"]
        )
    else:
        raise DeserializationError("MessageInsightsDataSource.end_date required")
    if "Include" in data:
        import aws_sdk_sesv2.types.message_insights_filters

        out["include"] = aws_sdk_sesv2.types.message_insights_filters.deserialize_json(
            data["Include"]
        )
    if "Exclude" in data:
        import aws_sdk_sesv2.types.message_insights_filters

        out["exclude"] = aws_sdk_sesv2.types.message_insights_filters.deserialize_json(
            data["Exclude"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out

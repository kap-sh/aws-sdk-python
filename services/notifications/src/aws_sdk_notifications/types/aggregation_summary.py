"""Generated from Smithy shape ``com.amazonaws.notifications#AggregationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.aggregation_keys
    import aws_sdk_notifications.types.summarization_dimension_overview
    import aws_sdk_notifications.types.summarization_dimension_overviews


class AggregationSummary(TypedDict, closed=True):
    event_count: "int"
    """<p>Indicates the number of events associated with the aggregation key.</p>"""
    aggregated_by: "aws_sdk_notifications.types.aggregation_keys.AggregationKeys"
    """<p>Indicates the criteria or rules by which notifications have been grouped together.</p>"""
    aggregated_accounts: "aws_sdk_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    """<p>Indicates the Amazon Web Services accounts in the aggregation key.</p>"""
    aggregated_regions: "aws_sdk_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    """<p>Indicates the Amazon Web Services Regions in the aggregation key.</p>"""
    aggregated_organizational_units: NotRequired[
        "aws_sdk_notifications.types.summarization_dimension_overview.SummarizationDimensionOverview"
    ]
    """<p>Indicates the collection of organizational units that are involved in the aggregation key.</p>"""
    additional_summarization_dimensions: NotRequired[
        "aws_sdk_notifications.types.summarization_dimension_overviews.SummarizationDimensionOverviews"
    ]
    """<p>List of additional dimensions used to group and summarize data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationSummary) -> dict:
    out: dict = {}
    out["eventCount"] = value["event_count"]
    import aws_sdk_notifications.types.aggregation_keys

    out["aggregatedBy"] = aws_sdk_notifications.types.aggregation_keys.serialize_json(
        value["aggregated_by"]
    )
    import aws_sdk_notifications.types.summarization_dimension_overview

    out["aggregatedAccounts"] = (
        aws_sdk_notifications.types.summarization_dimension_overview.serialize_json(
            value["aggregated_accounts"]
        )
    )
    import aws_sdk_notifications.types.summarization_dimension_overview

    out["aggregatedRegions"] = (
        aws_sdk_notifications.types.summarization_dimension_overview.serialize_json(
            value["aggregated_regions"]
        )
    )
    if "aggregated_organizational_units" in value:
        import aws_sdk_notifications.types.summarization_dimension_overview

        out["aggregatedOrganizationalUnits"] = (
            aws_sdk_notifications.types.summarization_dimension_overview.serialize_json(
                value["aggregated_organizational_units"]
            )
        )
    if "additional_summarization_dimensions" in value:
        import aws_sdk_notifications.types.summarization_dimension_overviews

        out["additionalSummarizationDimensions"] = (
            aws_sdk_notifications.types.summarization_dimension_overviews.serialize_json(
                value["additional_summarization_dimensions"]
            )
        )
    return out


def deserialize_json(data: dict) -> AggregationSummary:
    out: AggregationSummary = {}  # type: ignore[typeddict-item]
    if "eventCount" in data:
        out["event_count"] = data["eventCount"]
    else:
        raise DeserializationError("AggregationSummary.event_count required")
    if "aggregatedBy" in data:
        import aws_sdk_notifications.types.aggregation_keys

        out["aggregated_by"] = (
            aws_sdk_notifications.types.aggregation_keys.deserialize_json(
                data["aggregatedBy"]
            )
        )
    else:
        raise DeserializationError("AggregationSummary.aggregated_by required")
    if "aggregatedAccounts" in data:
        import aws_sdk_notifications.types.summarization_dimension_overview

        out["aggregated_accounts"] = (
            aws_sdk_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedAccounts"]
            )
        )
    else:
        raise DeserializationError("AggregationSummary.aggregated_accounts required")
    if "aggregatedRegions" in data:
        import aws_sdk_notifications.types.summarization_dimension_overview

        out["aggregated_regions"] = (
            aws_sdk_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedRegions"]
            )
        )
    else:
        raise DeserializationError("AggregationSummary.aggregated_regions required")
    if "aggregatedOrganizationalUnits" in data:
        import aws_sdk_notifications.types.summarization_dimension_overview

        out["aggregated_organizational_units"] = (
            aws_sdk_notifications.types.summarization_dimension_overview.deserialize_json(
                data["aggregatedOrganizationalUnits"]
            )
        )
    if "additionalSummarizationDimensions" in data:
        import aws_sdk_notifications.types.summarization_dimension_overviews

        out["additional_summarization_dimensions"] = (
            aws_sdk_notifications.types.summarization_dimension_overviews.deserialize_json(
                data["additionalSummarizationDimensions"]
            )
        )
    return out

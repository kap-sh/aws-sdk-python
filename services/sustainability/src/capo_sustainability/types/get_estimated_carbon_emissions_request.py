"""Generated from Smithy shape ``com.amazonaws.sustainability#GetEstimatedCarbonEmissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sustainability.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sustainability.types.dimension_list
    import capo_sustainability.types.emissions_type_list
    import capo_sustainability.types.filter_expression
    import capo_sustainability.types.granularity_configuration
    import capo_sustainability.types.max_results
    import capo_sustainability.types.next_token
    import capo_sustainability.types.time_granularity
    import capo_sustainability.types.time_period


class GetEstimatedCarbonEmissionsRequest(TypedDict, closed=True):
    time_period: "capo_sustainability.types.time_period.TimePeriod"
    """<p>The date range for fetching estimated carbon emissions.</p>"""
    group_by: NotRequired["capo_sustainability.types.dimension_list.DimensionList"]
    """<p>The dimensions available for grouping estimated carbon emissions.</p>"""
    filter_by: NotRequired[
        "capo_sustainability.types.filter_expression.FilterExpression"
    ]
    """<p>The criteria for filtering estimated carbon emissions.</p>"""
    emissions_types: NotRequired[
        "capo_sustainability.types.emissions_type_list.EmissionsTypeList"
    ]
    """<p>The emission types to include in the results. If absent, returns <code>TOTAL_LBM_CARBON_EMISSIONS</code> and <code>TOTAL_MBM_CARBON_EMISSIONS</code> emissions types. </p>"""
    granularity: "capo_sustainability.types.time_granularity.TimeGranularity"
    """<p>The time granularity for the results. If absent, uses <code>MONTHLY</code> time granularity.</p>"""
    granularity_configuration: NotRequired[
        "capo_sustainability.types.granularity_configuration.GranularityConfiguration"
    ]
    """<p>Configuration for fiscal year calculations when using <code>YEARLY_FISCAL</code> or <code>QUARTERLY_FISCAL</code> granularity. </p>"""
    max_results: "capo_sustainability.types.max_results.MaxResults"
    """<p>The maximum number of results to return in a single call. Default is 40.</p>"""
    next_token: NotRequired["capo_sustainability.types.next_token.NextToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEstimatedCarbonEmissionsRequest) -> dict:
    out: dict = {}
    import capo_sustainability.types.time_period

    out["TimePeriod"] = capo_sustainability.types.time_period.serialize_json(
        value["time_period"]
    )
    if "group_by" in value:
        import capo_sustainability.types.dimension_list

        out["GroupBy"] = capo_sustainability.types.dimension_list.serialize_json(
            value["group_by"]
        )
    if "filter_by" in value:
        import capo_sustainability.types.filter_expression

        out["FilterBy"] = capo_sustainability.types.filter_expression.serialize_json(
            value["filter_by"]
        )
    if "emissions_types" in value:
        import capo_sustainability.types.emissions_type_list

        out["EmissionsTypes"] = (
            capo_sustainability.types.emissions_type_list.serialize_json(
                value["emissions_types"]
            )
        )
    import capo_sustainability.types.time_granularity

    out["Granularity"] = capo_sustainability.types.time_granularity.serialize_json(
        value.get("granularity", "MONTHLY")
    )
    if "granularity_configuration" in value:
        import capo_sustainability.types.granularity_configuration

        out["GranularityConfiguration"] = (
            capo_sustainability.types.granularity_configuration.serialize_json(
                value["granularity_configuration"]
            )
        )
    out["MaxResults"] = value.get("max_results", 1000)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEstimatedCarbonEmissionsRequest:
    out: GetEstimatedCarbonEmissionsRequest = {}  # type: ignore[typeddict-item]
    if "TimePeriod" in data:
        import capo_sustainability.types.time_period

        out["time_period"] = capo_sustainability.types.time_period.deserialize_json(
            data["TimePeriod"]
        )
    else:
        raise DeserializationError(
            "GetEstimatedCarbonEmissionsRequest.time_period required"
        )
    if "GroupBy" in data:
        import capo_sustainability.types.dimension_list

        out["group_by"] = capo_sustainability.types.dimension_list.deserialize_json(
            data["GroupBy"]
        )
    if "FilterBy" in data:
        import capo_sustainability.types.filter_expression

        out["filter_by"] = capo_sustainability.types.filter_expression.deserialize_json(
            data["FilterBy"]
        )
    if "EmissionsTypes" in data:
        import capo_sustainability.types.emissions_type_list

        out["emissions_types"] = (
            capo_sustainability.types.emissions_type_list.deserialize_json(
                data["EmissionsTypes"]
            )
        )
    if "Granularity" in data:
        import capo_sustainability.types.time_granularity

        out["granularity"] = (
            capo_sustainability.types.time_granularity.deserialize_json(
                data["Granularity"]
            )
        )
    else:
        out["granularity"] = "MONTHLY"
    if "GranularityConfiguration" in data:
        import capo_sustainability.types.granularity_configuration

        out["granularity_configuration"] = (
            capo_sustainability.types.granularity_configuration.deserialize_json(
                data["GranularityConfiguration"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 1000
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

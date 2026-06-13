"""Generated from Smithy shape ``com.amazonaws.datazone#SearchListingsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_list
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_clause
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.search_in_list
    import aws_sdk_datazone.types.search_output_additional_attributes
    import aws_sdk_datazone.types.search_sort


class SearchListingsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which to search listings.</p>"""
    search_text: NotRequired["str"]
    """<p>Specifies the text for which to search.</p>"""
    search_in: NotRequired["aws_sdk_datazone.types.search_in_list.SearchInList"]
    """<p>The details of the search.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call to <code>SearchListings</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchListings</code> to list the next set of results. </p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchListings</code> to list the next set of results.</p>"""
    filters: NotRequired["aws_sdk_datazone.types.filter_clause.FilterClause"]
    """<p>Specifies the filters for the search of listings.</p>"""
    aggregations: NotRequired["aws_sdk_datazone.types.aggregation_list.AggregationList"]
    """<p>Enables you to specify one or more attributes to compute and return counts grouped by field values.</p>"""
    sort: NotRequired["aws_sdk_datazone.types.search_sort.SearchSort"]
    """<p>Specifies the way for sorting the search results.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
    ]
    """<p>Specifies additional attributes for the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchListingsInput) -> dict:
    out: dict = {}
    if "search_text" in value:
        out["searchText"] = value["search_text"]
    if "search_in" in value:
        import aws_sdk_datazone.types.search_in_list

        out["searchIn"] = aws_sdk_datazone.types.search_in_list.serialize_json(
            value["search_in"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_datazone.types.filter_clause

        out["filters"] = aws_sdk_datazone.types.filter_clause.serialize_json(
            value["filters"]
        )
    if "aggregations" in value:
        import aws_sdk_datazone.types.aggregation_list

        out["aggregations"] = aws_sdk_datazone.types.aggregation_list.serialize_json(
            value["aggregations"]
        )
    if "sort" in value:
        import aws_sdk_datazone.types.search_sort

        out["sort"] = aws_sdk_datazone.types.search_sort.serialize_json(value["sort"])
    if "additional_attributes" in value:
        import aws_sdk_datazone.types.search_output_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.search_output_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchListingsInput:
    out: SearchListingsInput = {}  # type: ignore[typeddict-item]
    if "searchText" in data:
        out["search_text"] = data["searchText"]
    if "searchIn" in data:
        import aws_sdk_datazone.types.search_in_list

        out["search_in"] = aws_sdk_datazone.types.search_in_list.deserialize_json(
            data["searchIn"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "filters" in data:
        import aws_sdk_datazone.types.filter_clause

        out["filters"] = aws_sdk_datazone.types.filter_clause.deserialize_json(
            data["filters"]
        )
    if "aggregations" in data:
        import aws_sdk_datazone.types.aggregation_list

        out["aggregations"] = aws_sdk_datazone.types.aggregation_list.deserialize_json(
            data["aggregations"]
        )
    if "sort" in data:
        import aws_sdk_datazone.types.search_sort

        out["sort"] = aws_sdk_datazone.types.search_sort.deserialize_json(data["sort"])
    if "additionalAttributes" in data:
        import aws_sdk_datazone.types.search_output_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.search_output_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    return out

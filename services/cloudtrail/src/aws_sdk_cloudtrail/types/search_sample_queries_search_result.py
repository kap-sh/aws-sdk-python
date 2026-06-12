"""Generated from Smithy shape ``com.amazonaws.cloudtrail#SearchSampleQueriesSearchResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.sample_query_description
    import aws_sdk_cloudtrail.types.sample_query_name
    import aws_sdk_cloudtrail.types.sample_query_relevance
    import aws_sdk_cloudtrail.types.sample_query_sql


class SearchSampleQueriesSearchResult(TypedDict):
    name: NotRequired["aws_sdk_cloudtrail.types.sample_query_name.SampleQueryName"]
    """<p> The name of a sample query. </p>"""
    description: NotRequired[
        "aws_sdk_cloudtrail.types.sample_query_description.SampleQueryDescription"
    ]
    """<p> A longer description of a sample query. </p>"""
    sql: NotRequired["aws_sdk_cloudtrail.types.sample_query_sql.SampleQuerySQL"]
    """<p> The SQL code of the sample query. </p>"""
    relevance: "aws_sdk_cloudtrail.types.sample_query_relevance.SampleQueryRelevance"
    """<p> A value between 0 and 1 indicating the similarity between the search phrase and result. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSampleQueriesSearchResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "sql" in value:
        out["SQL"] = value["sql"]
    out["Relevance"] = value.get("relevance", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSampleQueriesSearchResult:
    out: SearchSampleQueriesSearchResult = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SQL" in data:
        out["sql"] = data["SQL"]
    if "Relevance" in data:
        out["relevance"] = data["Relevance"]
    else:
        out["relevance"] = 0
    return out

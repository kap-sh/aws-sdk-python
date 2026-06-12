"""Generated from Smithy shape ``com.amazonaws.glue#SearchTablesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean_nullable
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.resource_share_type
    import aws_sdk_glue.types.search_property_predicates
    import aws_sdk_glue.types.sort_criteria
    import aws_sdk_glue.types.token
    import aws_sdk_glue.types.value_string


class SearchTablesRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>A unique identifier, consisting of <code> <i>account_id</i> </code>.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    filters: NotRequired[
        "aws_sdk_glue.types.search_property_predicates.SearchPropertyPredicates"
    ]
    """<p>A list of key-value pairs, and a comparator used to filter the search results. Returns all entities matching the predicate.</p> <p>The <code>Comparator</code> member of the <code>PropertyPredicate</code> struct is used only for time fields, and can be omitted for other field types. Also, when comparing string values, such as when <code>Key=Name</code>, a fuzzy match algorithm is used. The <code>Key</code> field (for example, the value of the <code>Name</code> field) is split on certain punctuation characters, for example, -, :, #, etc. into tokens. Then each token is exact-match compared with the <code>Value</code> member of <code>PropertyPredicate</code>. For example, if <code>Key=Name</code> and <code>Value=link</code>, tables named <code>customer-link</code> and <code>xx-link-yy</code> are returned, but <code>xxlinkyy</code> is not returned.</p>"""
    search_text: NotRequired["aws_sdk_glue.types.value_string.ValueString"]
    """<p>A string used for a text search.</p> <p>Specifying a value in quotes filters based on an exact match to the value.</p>"""
    sort_criteria: NotRequired["aws_sdk_glue.types.sort_criteria.SortCriteria"]
    """<p>A list of criteria for sorting the results by a field name, in an ascending or descending order.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum number of tables to return in a single response.</p>"""
    resource_share_type: NotRequired[
        "aws_sdk_glue.types.resource_share_type.ResourceShareType"
    ]
    """<p>Allows you to specify that you want to search the tables shared with your account. The allowable values are <code>FOREIGN</code> or <code>ALL</code>. </p> <ul> <li> <p>If set to <code>FOREIGN</code>, will search the tables shared with your account. </p> </li> <li> <p>If set to <code>ALL</code>, will search the tables shared with your account, as well as the tables in yor local account. </p> </li> </ul>"""
    include_status_details: NotRequired[
        "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
    ]
    """<p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchTablesRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_glue.types.search_property_predicates

        out["Filters"] = (
            aws_sdk_glue.types.search_property_predicates.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "search_text" in value:
        out["SearchText"] = value["search_text"]
    if "sort_criteria" in value:
        import aws_sdk_glue.types.sort_criteria

        out["SortCriteria"] = aws_sdk_glue.types.sort_criteria.serialize_aws_json_1_1(
            value["sort_criteria"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "resource_share_type" in value:
        import aws_sdk_glue.types.resource_share_type

        out["ResourceShareType"] = (
            aws_sdk_glue.types.resource_share_type.serialize_aws_json_1_1(
                value["resource_share_type"]
            )
        )
    if "include_status_details" in value:
        out["IncludeStatusDetails"] = value["include_status_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchTablesRequest:
    out: SearchTablesRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_glue.types.search_property_predicates

        out["filters"] = (
            aws_sdk_glue.types.search_property_predicates.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "SearchText" in data:
        out["search_text"] = data["SearchText"]
    if "SortCriteria" in data:
        import aws_sdk_glue.types.sort_criteria

        out["sort_criteria"] = (
            aws_sdk_glue.types.sort_criteria.deserialize_aws_json_1_1(
                data["SortCriteria"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "ResourceShareType" in data:
        import aws_sdk_glue.types.resource_share_type

        out["resource_share_type"] = (
            aws_sdk_glue.types.resource_share_type.deserialize_aws_json_1_1(
                data["ResourceShareType"]
            )
        )
    if "IncludeStatusDetails" in data:
        out["include_status_details"] = data["IncludeStatusDetails"]
    return out

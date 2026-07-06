"""Generated from Smithy shape ``com.amazonaws.glue#ListMaterializedViewRefreshTaskRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.page_size
    import aws_sdk_glue.types.token


class ListMaterializedViewRefreshTaskRunsRequest(TypedDict, closed=True):
    catalog_id: "aws_sdk_glue.types.name_string.NameString"
    """<p>The ID of the Data Catalog where the table resides. If none is supplied, the account ID is used by default.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The database where the table resides.</p>"""
    table_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the table for which statistics is generated.</p>"""
    max_results: NotRequired["aws_sdk_glue.types.page_size.PageSize"]
    """<p>The maximum size of the response.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMaterializedViewRefreshTaskRunsRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMaterializedViewRefreshTaskRunsRequest:
    out: ListMaterializedViewRefreshTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError(
            "ListMaterializedViewRefreshTaskRunsRequest.catalog_id required"
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

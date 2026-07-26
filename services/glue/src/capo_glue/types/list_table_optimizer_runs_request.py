"""Generated from Smithy shape ``com.amazonaws.glue#ListTableOptimizerRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.list_table_optimizer_runs_token
    import capo_glue.types.max_list_table_optimizer_runs_token_results
    import capo_glue.types.name_string
    import capo_glue.types.table_optimizer_type


class ListTableOptimizerRunsRequest(TypedDict, closed=True):
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The Catalog ID of the table.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    type: "capo_glue.types.table_optimizer_type.TableOptimizerType"
    """<p>The type of table optimizer.</p>"""
    max_results: "capo_glue.types.max_list_table_optimizer_runs_token_results.MaxListTableOptimizerRunsTokenResults"
    """<p>The maximum number of optimizer runs to return on each call.</p>"""
    next_token: NotRequired[
        "capo_glue.types.list_table_optimizer_runs_token.ListTableOptimizerRunsToken"
    ]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTableOptimizerRunsRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.table_optimizer_type

    out["Type"] = capo_glue.types.table_optimizer_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTableOptimizerRunsRequest:
    out: ListTableOptimizerRunsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("ListTableOptimizerRunsRequest.catalog_id required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "ListTableOptimizerRunsRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("ListTableOptimizerRunsRequest.table_name required")
    if "Type" in data:
        import capo_glue.types.table_optimizer_type

        out["type"] = capo_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("ListTableOptimizerRunsRequest.type required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

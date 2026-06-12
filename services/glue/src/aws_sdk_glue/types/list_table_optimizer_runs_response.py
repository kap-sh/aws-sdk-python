"""Generated from Smithy shape ``com.amazonaws.glue#ListTableOptimizerRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.list_table_optimizer_runs_token
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.table_optimizer_runs


class ListTableOptimizerRunsResponse(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The Catalog ID of the table.</p>"""
    database_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the table.</p>"""
    next_token: NotRequired[
        "aws_sdk_glue.types.list_table_optimizer_runs_token.ListTableOptimizerRunsToken"
    ]
    """<p>A continuation token for paginating the returned list of optimizer runs, returned if the current segment of the list is not the last.</p>"""
    table_optimizer_runs: NotRequired[
        "aws_sdk_glue.types.table_optimizer_runs.TableOptimizerRuns"
    ]
    """<p>A list of the optimizer runs associated with a table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTableOptimizerRunsResponse) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "table_optimizer_runs" in value:
        import aws_sdk_glue.types.table_optimizer_runs

        out["TableOptimizerRuns"] = (
            aws_sdk_glue.types.table_optimizer_runs.serialize_aws_json_1_1(
                value["table_optimizer_runs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTableOptimizerRunsResponse:
    out: ListTableOptimizerRunsResponse = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TableOptimizerRuns" in data:
        import aws_sdk_glue.types.table_optimizer_runs

        out["table_optimizer_runs"] = (
            aws_sdk_glue.types.table_optimizer_runs.deserialize_aws_json_1_1(
                data["TableOptimizerRuns"]
            )
        )
    return out

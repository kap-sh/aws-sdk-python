"""Generated from Smithy shape ``com.amazonaws.glue#GetTableVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.catalog_getter_page_size
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.token


class GetTableVersionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table. For Hive compatibility, this name is entirely lowercase.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is not the first call.</p>"""
    max_results: NotRequired[
        "capo_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
    ]
    """<p>The maximum number of table versions to return in one response.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableVersionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "audit_context" in value:
        import capo_glue.types.audit_context

        out["AuditContext"] = capo_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableVersionsRequest:
    out: GetTableVersionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableVersionsRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetTableVersionsRequest.table_name required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "AuditContext" in data:
        import capo_glue.types.audit_context

        out["audit_context"] = capo_glue.types.audit_context.deserialize_aws_json_1_1(
            data["AuditContext"]
        )
    return out

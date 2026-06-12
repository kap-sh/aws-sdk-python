"""Generated from Smithy shape ``com.amazonaws.glue#GetTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.audit_context
    import aws_sdk_glue.types.boolean_nullable
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.transaction_id_string


class GetTableRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the table contents. </p>"""
    query_as_of_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    audit_context: NotRequired["aws_sdk_glue.types.audit_context.AuditContext"]
    """<p>A structure containing the Lake Formation <a href=\"https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html\">audit context</a>.</p>"""
    include_status_details: NotRequired[
        "aws_sdk_glue.types.boolean_nullable.BooleanNullable"
    ]
    """<p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["Name"] = value["name"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "query_as_of_time" in value:
        import aws_sdk_glue.types.timestamp

        out["QueryAsOfTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["query_as_of_time"]
        )
    if "audit_context" in value:
        import aws_sdk_glue.types.audit_context

        out["AuditContext"] = aws_sdk_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    if "include_status_details" in value:
        out["IncludeStatusDetails"] = value["include_status_details"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTableRequest:
    out: GetTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableRequest.database_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetTableRequest.name required")
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    if "QueryAsOfTime" in data:
        import aws_sdk_glue.types.timestamp

        out["query_as_of_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["QueryAsOfTime"]
        )
    if "AuditContext" in data:
        import aws_sdk_glue.types.audit_context

        out["audit_context"] = (
            aws_sdk_glue.types.audit_context.deserialize_aws_json_1_1(
                data["AuditContext"]
            )
        )
    if "IncludeStatusDetails" in data:
        out["include_status_details"] = data["IncludeStatusDetails"]
    return out

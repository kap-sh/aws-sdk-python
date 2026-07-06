"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetPartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.audit_context
    import aws_sdk_glue.types.batch_get_partition_value_list
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.query_session_context


class BatchGetPartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    partitions_to_get: (
        "aws_sdk_glue.types.batch_get_partition_value_list.BatchGetPartitionValueList"
    )
    """<p>A list of partition values identifying the partitions to retrieve.</p>"""
    audit_context: NotRequired["aws_sdk_glue.types.audit_context.AuditContext"]
    query_session_context: NotRequired[
        "aws_sdk_glue.types.query_session_context.QuerySessionContext"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.batch_get_partition_value_list

    out["PartitionsToGet"] = (
        aws_sdk_glue.types.batch_get_partition_value_list.serialize_aws_json_1_1(
            value["partitions_to_get"]
        )
    )
    if "audit_context" in value:
        import aws_sdk_glue.types.audit_context

        out["AuditContext"] = aws_sdk_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    if "query_session_context" in value:
        import aws_sdk_glue.types.query_session_context

        out["QuerySessionContext"] = (
            aws_sdk_glue.types.query_session_context.serialize_aws_json_1_1(
                value["query_session_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPartitionRequest:
    out: BatchGetPartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("BatchGetPartitionRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("BatchGetPartitionRequest.table_name required")
    if "PartitionsToGet" in data:
        import aws_sdk_glue.types.batch_get_partition_value_list

        out["partitions_to_get"] = (
            aws_sdk_glue.types.batch_get_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionsToGet"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetPartitionRequest.partitions_to_get required"
        )
    if "AuditContext" in data:
        import aws_sdk_glue.types.audit_context

        out["audit_context"] = (
            aws_sdk_glue.types.audit_context.deserialize_aws_json_1_1(
                data["AuditContext"]
            )
        )
    if "QuerySessionContext" in data:
        import aws_sdk_glue.types.query_session_context

        out["query_session_context"] = (
            aws_sdk_glue.types.query_session_context.deserialize_aws_json_1_1(
                data["QuerySessionContext"]
            )
        )
    return out

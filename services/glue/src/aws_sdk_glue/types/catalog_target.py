"""Generated from Smithy shape ``com.amazonaws.glue#CatalogTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_tables_list
    import aws_sdk_glue.types.connection_name
    import aws_sdk_glue.types.event_queue_arn
    import aws_sdk_glue.types.name_string


class CatalogTarget(TypedDict):
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database to be synchronized.</p>"""
    tables: "aws_sdk_glue.types.catalog_tables_list.CatalogTablesList"
    """<p>A list of the tables to be synchronized.</p>"""
    connection_name: NotRequired["aws_sdk_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection for an Amazon S3-backed Data Catalog table to be a target of the crawl when using a <code>Catalog</code> connection type paired with a <code>NETWORK</code> Connection type.</p>"""
    event_queue_arn: NotRequired["aws_sdk_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon SQS ARN. For example, <code>arn:aws:sqs:region:account:sqs</code>.</p>"""
    dlq_event_queue_arn: NotRequired["aws_sdk_glue.types.event_queue_arn.EventQueueArn"]
    """<p>A valid Amazon dead-letter SQS ARN. For example, <code>arn:aws:sqs:region:account:deadLetterQueue</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogTarget) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    import aws_sdk_glue.types.catalog_tables_list

    out["Tables"] = aws_sdk_glue.types.catalog_tables_list.serialize_aws_json_1_1(
        value["tables"]
    )
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "event_queue_arn" in value:
        out["EventQueueArn"] = value["event_queue_arn"]
    if "dlq_event_queue_arn" in value:
        out["DlqEventQueueArn"] = value["dlq_event_queue_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogTarget:
    out: CatalogTarget = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CatalogTarget.database_name required")
    if "Tables" in data:
        import aws_sdk_glue.types.catalog_tables_list

        out["tables"] = aws_sdk_glue.types.catalog_tables_list.deserialize_aws_json_1_1(
            data["Tables"]
        )
    else:
        raise DeserializationError("CatalogTarget.tables required")
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "EventQueueArn" in data:
        out["event_queue_arn"] = data["EventQueueArn"]
    if "DlqEventQueueArn" in data:
        out["dlq_event_queue_arn"] = data["DlqEventQueueArn"]
    return out

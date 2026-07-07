"""Generated from Smithy shape ``com.amazonaws.s3tables#TableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3tables.types.namespace_id
    import aws_sdk_s3tables.types.namespace_list
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_bucket_id
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.table_type


class TableSummary(TypedDict, closed=True):
    namespace: "aws_sdk_s3tables.types.namespace_list.NamespaceList"
    """<p>The name of the namespace.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    type: "aws_sdk_s3tables.types.table_type.TableType"
    """<p>The type of the table.</p>"""
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table was created at.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the table was last modified at.</p>"""
    managed_by_service: NotRequired["str"]
    """<p>The Amazon Web Services service managing this table, if applicable. For example, a replicated table is managed by the S3 Tables replication service.</p>"""
    namespace_id: NotRequired["aws_sdk_s3tables.types.namespace_id.NamespaceId"]
    """<p>The unique identifier for the namespace that contains this table.</p>"""
    table_bucket_id: NotRequired["aws_sdk_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier for the table bucket that contains this table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSummary) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.namespace_list

    out["namespace"] = aws_sdk_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    out["name"] = value["name"]
    import aws_sdk_s3tables.types.table_type

    out["type"] = aws_sdk_s3tables.types.table_type.serialize_json(value["type"])
    out["tableARN"] = value["table_arn"]
    import aws_sdk_s3tables.types._prelude.timestamp

    out["createdAt"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_s3tables.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "managed_by_service" in value:
        out["managedByService"] = value["managed_by_service"]
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    return out


def deserialize_json(data: dict) -> TableSummary:
    out: TableSummary = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_s3tables.types.namespace_list

        out["namespace"] = aws_sdk_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        raise DeserializationError("TableSummary.namespace required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TableSummary.name required")
    if "type" in data:
        import aws_sdk_s3tables.types.table_type

        out["type"] = aws_sdk_s3tables.types.table_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("TableSummary.type required")
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError("TableSummary.table_arn required")
    if "createdAt" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["created_at"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("TableSummary.created_at required")
    if "modifiedAt" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["modified_at"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError("TableSummary.modified_at required")
    if "managedByService" in data:
        out["managed_by_service"] = data["managedByService"]
    if "namespaceId" in data:
        out["namespace_id"] = data["namespaceId"]
    if "tableBucketId" in data:
        out["table_bucket_id"] = data["tableBucketId"]
    return out

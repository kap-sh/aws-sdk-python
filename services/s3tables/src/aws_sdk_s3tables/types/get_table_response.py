"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3tables.types.account_id
    import aws_sdk_s3tables.types.managed_table_information
    import aws_sdk_s3tables.types.metadata_location
    import aws_sdk_s3tables.types.namespace_id
    import aws_sdk_s3tables.types.namespace_list
    import aws_sdk_s3tables.types.open_table_format
    import aws_sdk_s3tables.types.table_arn
    import aws_sdk_s3tables.types.table_bucket_id
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.table_type
    import aws_sdk_s3tables.types.version_token
    import aws_sdk_s3tables.types.warehouse_location


class GetTableResponse(TypedDict):
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    type: "aws_sdk_s3tables.types.table_type.TableType"
    """<p>The type of the table.</p>"""
    table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    namespace: "aws_sdk_s3tables.types.namespace_list.NamespaceList"
    """<p>The namespace associated with the table.</p>"""
    namespace_id: NotRequired["aws_sdk_s3tables.types.namespace_id.NamespaceId"]
    """<p>The unique identifier of the namespace containing this table.</p>"""
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""
    metadata_location: NotRequired[
        "aws_sdk_s3tables.types.metadata_location.MetadataLocation"
    ]
    """<p>The metadata location of the table.</p>"""
    warehouse_location: "aws_sdk_s3tables.types.warehouse_location.WarehouseLocation"
    """<p>The warehouse location of the table.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table bucket was created at.</p>"""
    created_by: "aws_sdk_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that created the table.</p>"""
    managed_by_service: NotRequired["str"]
    """<p>The service that manages the table.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the table was last modified on.</p>"""
    modified_by: "aws_sdk_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that last modified the table.</p>"""
    owner_account_id: "aws_sdk_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that owns the table.</p>"""
    format: "aws_sdk_s3tables.types.open_table_format.OpenTableFormat"
    """<p>The format of the table.</p>"""
    table_bucket_id: NotRequired["aws_sdk_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier of the table bucket containing this table.</p>"""
    managed_table_information: NotRequired[
        "aws_sdk_s3tables.types.managed_table_information.ManagedTableInformation"
    ]
    """<p>If this table is managed by S3 Tables, contains additional information such as replication details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_s3tables.types.table_type

    out["type"] = aws_sdk_s3tables.types.table_type.serialize_json(value["type"])
    out["tableARN"] = value["table_arn"]
    import aws_sdk_s3tables.types.namespace_list

    out["namespace"] = aws_sdk_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    out["versionToken"] = value["version_token"]
    if "metadata_location" in value:
        out["metadataLocation"] = value["metadata_location"]
    out["warehouseLocation"] = value["warehouse_location"]
    import aws_sdk_s3tables.types._prelude.timestamp

    out["createdAt"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "managed_by_service" in value:
        out["managedByService"] = value["managed_by_service"]
    import aws_sdk_s3tables.types._prelude.timestamp

    out["modifiedAt"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    out["modifiedBy"] = value["modified_by"]
    out["ownerAccountId"] = value["owner_account_id"]
    import aws_sdk_s3tables.types.open_table_format

    out["format"] = aws_sdk_s3tables.types.open_table_format.serialize_json(
        value["format"]
    )
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    if "managed_table_information" in value:
        import aws_sdk_s3tables.types.managed_table_information

        out["managedTableInformation"] = (
            aws_sdk_s3tables.types.managed_table_information.serialize_json(
                value["managed_table_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetTableResponse.name required")
    if "type" in data:
        import aws_sdk_s3tables.types.table_type

        out["type"] = aws_sdk_s3tables.types.table_type.deserialize_json(data["type"])
    else:
        raise DeserializationError("GetTableResponse.type required")
    if "tableARN" in data:
        out["table_arn"] = data["tableARN"]
    else:
        raise DeserializationError("GetTableResponse.table_arn required")
    if "namespace" in data:
        import aws_sdk_s3tables.types.namespace_list

        out["namespace"] = aws_sdk_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        raise DeserializationError("GetTableResponse.namespace required")
    if "namespaceId" in data:
        out["namespace_id"] = data["namespaceId"]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError("GetTableResponse.version_token required")
    if "metadataLocation" in data:
        out["metadata_location"] = data["metadataLocation"]
    if "warehouseLocation" in data:
        out["warehouse_location"] = data["warehouseLocation"]
    else:
        raise DeserializationError("GetTableResponse.warehouse_location required")
    if "createdAt" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["created_at"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetTableResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetTableResponse.created_by required")
    if "managedByService" in data:
        out["managed_by_service"] = data["managedByService"]
    if "modifiedAt" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["modified_at"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["modifiedAt"]
        )
    else:
        raise DeserializationError("GetTableResponse.modified_at required")
    if "modifiedBy" in data:
        out["modified_by"] = data["modifiedBy"]
    else:
        raise DeserializationError("GetTableResponse.modified_by required")
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError("GetTableResponse.owner_account_id required")
    if "format" in data:
        import aws_sdk_s3tables.types.open_table_format

        out["format"] = aws_sdk_s3tables.types.open_table_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("GetTableResponse.format required")
    if "tableBucketId" in data:
        out["table_bucket_id"] = data["tableBucketId"]
    if "managedTableInformation" in data:
        import aws_sdk_s3tables.types.managed_table_information

        out["managed_table_information"] = (
            aws_sdk_s3tables.types.managed_table_information.deserialize_json(
                data["managedTableInformation"]
            )
        )
    return out

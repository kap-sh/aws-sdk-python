"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableGlobalSecondaryIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_projection
    import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.size_bytes


class AwsDynamoDbTableGlobalSecondaryIndex(TypedDict, closed=True):
    backfilling: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the index is currently backfilling.</p>"""
    index_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the index.</p>"""
    index_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the index.</p>"""
    index_size_bytes: NotRequired["aws_sdk_securityhub.types.size_bytes.SizeBytes"]
    """<p>The total size in bytes of the index.</p>"""
    index_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The current status of the index.</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATING</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>UPDATING</code> </p> </li> </ul>"""
    item_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of items in the index.</p>"""
    key_schema: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.AwsDynamoDbTableKeySchemaList"
    ]
    """<p>The key schema for the index.</p>"""
    projection: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_projection.AwsDynamoDbTableProjection"
    ]
    """<p>Attributes that are copied from the table into an index.</p>"""
    provisioned_throughput: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.AwsDynamoDbTableProvisionedThroughput"
    ]
    """<p>Information about the provisioned throughput settings for the indexes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableGlobalSecondaryIndex) -> dict:
    out: dict = {}
    if "backfilling" in value:
        out["Backfilling"] = value["backfilling"]
    if "index_arn" in value:
        out["IndexArn"] = value["index_arn"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "index_size_bytes" in value:
        out["IndexSizeBytes"] = value["index_size_bytes"]
    if "index_status" in value:
        out["IndexStatus"] = value["index_status"]
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "key_schema" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["KeySchema"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.serialize_json(
                value["key_schema"]
            )
        )
    if "projection" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_projection

        out["Projection"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_projection.serialize_json(
                value["projection"]
            )
        )
    if "provisioned_throughput" in value:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["ProvisionedThroughput"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.serialize_json(
                value["provisioned_throughput"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableGlobalSecondaryIndex:
    out: AwsDynamoDbTableGlobalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if "Backfilling" in data:
        out["backfilling"] = data["Backfilling"]
    if "IndexArn" in data:
        out["index_arn"] = data["IndexArn"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "IndexSizeBytes" in data:
        out["index_size_bytes"] = data["IndexSizeBytes"]
    if "IndexStatus" in data:
        out["index_status"] = data["IndexStatus"]
    if "ItemCount" in data:
        out["item_count"] = data["ItemCount"]
    if "KeySchema" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list

        out["key_schema"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.deserialize_json(
                data["KeySchema"]
            )
        )
    if "Projection" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_projection

        out["projection"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_projection.deserialize_json(
                data["Projection"]
            )
        )
    if "ProvisionedThroughput" in data:
        import aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput

        out["provisioned_throughput"] = (
            aws_sdk_securityhub.types.aws_dynamo_db_table_provisioned_throughput.deserialize_json(
                data["ProvisionedThroughput"]
            )
        )
    return out

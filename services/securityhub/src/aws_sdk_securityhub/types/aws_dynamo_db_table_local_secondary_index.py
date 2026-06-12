"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableLocalSecondaryIndex``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list
    import aws_sdk_securityhub.types.aws_dynamo_db_table_projection
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableLocalSecondaryIndex(TypedDict):
    index_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the index.</p>"""
    index_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the index.</p>"""
    key_schema: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_key_schema_list.AwsDynamoDbTableKeySchemaList"
    ]
    """<p>The complete key schema for the index.</p>"""
    projection: NotRequired[
        "aws_sdk_securityhub.types.aws_dynamo_db_table_projection.AwsDynamoDbTableProjection"
    ]
    """<p>Attributes that are copied from the table into the index. These are in addition to the primary key attributes and index key attributes, which are automatically projected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableLocalSecondaryIndex) -> dict:
    out: dict = {}
    if "index_arn" in value:
        out["IndexArn"] = value["index_arn"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
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
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableLocalSecondaryIndex:
    out: AwsDynamoDbTableLocalSecondaryIndex = {}  # type: ignore[typeddict-item]
    if "IndexArn" in data:
        out["index_arn"] = data["IndexArn"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
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
    return out

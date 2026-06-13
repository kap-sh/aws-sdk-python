"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3tables.types.account_id
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_bucket_id
    import aws_sdk_s3tables.types.table_bucket_name
    import aws_sdk_s3tables.types.table_bucket_type


class TableBucketSummary(TypedDict):
    arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    name: "aws_sdk_s3tables.types.table_bucket_name.TableBucketName"
    """<p>The name of the table bucket.</p>"""
    owner_account_id: "aws_sdk_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that owns the table bucket.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table bucket was created at.</p>"""
    table_bucket_id: NotRequired["aws_sdk_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The system-assigned unique identifier for the table bucket.</p>"""
    type: NotRequired["aws_sdk_s3tables.types.table_bucket_type.TableBucketType"]
    """<p>The type of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableBucketSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["ownerAccountId"] = value["owner_account_id"]
    import aws_sdk_s3tables.types._prelude.timestamp

    out["createdAt"] = aws_sdk_s3tables.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    if "type" in value:
        import aws_sdk_s3tables.types.table_bucket_type

        out["type"] = aws_sdk_s3tables.types.table_bucket_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> TableBucketSummary:
    out: TableBucketSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("TableBucketSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TableBucketSummary.name required")
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError("TableBucketSummary.owner_account_id required")
    if "createdAt" in data:
        import aws_sdk_s3tables.types._prelude.timestamp

        out["created_at"] = aws_sdk_s3tables.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("TableBucketSummary.created_at required")
    if "tableBucketId" in data:
        out["table_bucket_id"] = data["tableBucketId"]
    if "type" in data:
        import aws_sdk_s3tables.types.table_bucket_type

        out["type"] = aws_sdk_s3tables.types.table_bucket_type.deserialize_json(
            data["type"]
        )
    return out

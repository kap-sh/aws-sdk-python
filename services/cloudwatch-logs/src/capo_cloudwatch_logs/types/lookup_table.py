"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LookupTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.records_count
    import capo_cloudwatch_logs.types.stored_bytes
    import capo_cloudwatch_logs.types.table_fields
    import capo_cloudwatch_logs.types.timestamp


class LookupTable(TypedDict, closed=True):
    lookup_table_arn: NotRequired["capo_cloudwatch_logs.types.arn.Arn"]
    """<p>The ARN of the lookup table.</p>"""
    lookup_table_name: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    ]
    """<p>The name of the lookup table.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>The description of the lookup table.</p>"""
    table_fields: NotRequired["capo_cloudwatch_logs.types.table_fields.TableFields"]
    """<p>The column headers from the first row of the CSV file.</p>"""
    records_count: NotRequired["capo_cloudwatch_logs.types.records_count.RecordsCount"]
    """<p>The number of data rows in the lookup table, excluding the header row.</p>"""
    size_bytes: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The size of the lookup table in bytes.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the lookup table was last updated, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key used to encrypt the lookup table data, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupTable) -> dict:
    out: dict = {}
    if "lookup_table_arn" in value:
        out["lookupTableArn"] = value["lookup_table_arn"]
    if "lookup_table_name" in value:
        out["lookupTableName"] = value["lookup_table_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "table_fields" in value:
        import capo_cloudwatch_logs.types.table_fields

        out["tableFields"] = (
            capo_cloudwatch_logs.types.table_fields.serialize_aws_json_1_1(
                value["table_fields"]
            )
        )
    if "records_count" in value:
        out["recordsCount"] = value["records_count"]
    if "size_bytes" in value:
        out["sizeBytes"] = value["size_bytes"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupTable:
    out: LookupTable = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableArn") is not None:
        out["lookup_table_arn"] = data["lookupTableArn"]
    if data.get("lookupTableName") is not None:
        out["lookup_table_name"] = data["lookupTableName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tableFields") is not None:
        import capo_cloudwatch_logs.types.table_fields

        out["table_fields"] = (
            capo_cloudwatch_logs.types.table_fields.deserialize_aws_json_1_1(
                data["tableFields"]
            )
        )
    if data.get("recordsCount") is not None:
        out["records_count"] = data["recordsCount"]
    if data.get("sizeBytes") is not None:
        out["size_bytes"] = data["sizeBytes"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out

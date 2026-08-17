"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLookupTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.stored_bytes
    import capo_cloudwatch_logs.types.table_body
    import capo_cloudwatch_logs.types.timestamp


class GetLookupTableResponse(TypedDict, closed=True):
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
    table_body: NotRequired["capo_cloudwatch_logs.types.table_body.TableBody"]
    """<p>The full CSV content of the lookup table.</p>"""
    size_bytes: NotRequired["capo_cloudwatch_logs.types.stored_bytes.StoredBytes"]
    """<p>The size of the lookup table in bytes.</p>"""
    last_updated_time: NotRequired["capo_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The time when the lookup table was last updated, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key used to encrypt the lookup table data, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLookupTableResponse) -> dict:
    out: dict = {}
    if "lookup_table_arn" in value:
        out["lookupTableArn"] = value["lookup_table_arn"]
    if "lookup_table_name" in value:
        out["lookupTableName"] = value["lookup_table_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "table_body" in value:
        out["tableBody"] = value["table_body"]
    if "size_bytes" in value:
        out["sizeBytes"] = value["size_bytes"]
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLookupTableResponse:
    out: GetLookupTableResponse = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableArn") is not None:
        out["lookup_table_arn"] = data["lookupTableArn"]
    if data.get("lookupTableName") is not None:
        out["lookup_table_name"] = data["lookupTableName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tableBody") is not None:
        out["table_body"] = data["tableBody"]
    if data.get("sizeBytes") is not None:
        out["size_bytes"] = data["sizeBytes"]
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out

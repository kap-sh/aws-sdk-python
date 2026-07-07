"""Generated from Smithy shape ``com.amazonaws.glue#DynamoDBTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.nullable_double
    import aws_sdk_glue.types.path


class DynamoDBTarget(TypedDict, closed=True):
    path: NotRequired["aws_sdk_glue.types.path.Path"]
    """<p>The name of the DynamoDB table to crawl.</p>"""
    scan_all: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.</p> <p>A value of <code>true</code> means to scan all records, while a value of <code>false</code> means to sample the records. If no value is specified, the value defaults to <code>true</code>.</p>"""
    scan_rate: NotRequired["aws_sdk_glue.types.nullable_double.NullableDouble"]
    """<p>The percentage of the configured read capacity units to use by the Glue crawler. Read capacity units is a term defined by DynamoDB, and is a numeric value that acts as rate limiter for the number of reads that can be performed on that table per second.</p> <p>The valid values are null or a value between 0.1 to 1.5. A null value is used when user does not provide a value, and defaults to 0.5 of the configured Read Capacity Unit (for provisioned tables), or 0.25 of the max configured Read Capacity Unit (for tables using on-demand mode).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamoDBTarget) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "scan_all" in value:
        out["scanAll"] = value["scan_all"]
    if "scan_rate" in value:
        out["scanRate"] = value["scan_rate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamoDBTarget:
    out: DynamoDBTarget = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    if "scanAll" in data:
        out["scan_all"] = data["scanAll"]
    if "scanRate" in data:
        out["scan_rate"] = data["scanRate"]
    return out

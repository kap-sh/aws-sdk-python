"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationPartition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string128


class IntegrationPartition(TypedDict, closed=True):
    field_name: NotRequired["capo_glue.types.string128.String128"]
    """<p>The field name used to partition data on the target. Avoid using columns that have unique values for each row (for example, `LastModifiedTimestamp`, `SystemModTimeStamp`) as the partition column. These columns are not suitable for partitioning because they create a large number of small partitions, which can lead to performance issues.</p>"""
    function_spec: NotRequired["capo_glue.types.string128.String128"]
    """<p>Specifies the function used to partition data on the target. The accepted values for this parameter are:</p> <ul> <li> <p> <code>identity</code> - Uses source values directly without transformation</p> </li> <li> <p> <code>year</code> - Extracts the year from timestamp values (e.g., 2023)</p> </li> <li> <p> <code>month</code> - Extracts the month from timestamp values (e.g., 2023-01)</p> </li> <li> <p> <code>day</code> - Extracts the day from timestamp values (e.g., 2023-01-15)</p> </li> <li> <p> <code>hour</code> - Extracts the hour from timestamp values (e.g., 2023-01-15-14)</p> </li> </ul>"""
    conversion_spec: NotRequired["capo_glue.types.string128.String128"]
    """<p>Specifies the timestamp format of the source data. Valid values are:</p> <ul> <li> <p> <code>epoch_sec</code> - Unix epoch timestamp in seconds</p> </li> <li> <p> <code>epoch_milli</code> - Unix epoch timestamp in milliseconds</p> </li> <li> <p> <code>iso</code> - ISO 8601 formatted timestamp</p> </li> </ul> <note> <p> Only specify <code>ConversionSpec</code> when using timestamp-based partition functions (year, month, day, or hour). Glue Zero-ETL uses this parameter to correctly transform source data into timestamp format before partitioning. </p> <p> Do not use high-cardinality columns with the <code>identity</code> partition function. High-cardinality columns include: </p> <ul> <li> <p>Primary keys</p> </li> <li> <p>Timestamp fields (such as <code>LastModifiedTimestamp</code>, <code>CreatedDate</code>)</p> </li> <li> <p>System-generated timestamps</p> </li> </ul> <p> Using high-cardinality columns with identity partitioning creates many small partitions, which can significantly degrade ingestion performance. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationPartition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "function_spec" in value:
        out["FunctionSpec"] = value["function_spec"]
    if "conversion_spec" in value:
        out["ConversionSpec"] = value["conversion_spec"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegrationPartition:
    out: IntegrationPartition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "FunctionSpec" in data:
        out["function_spec"] = data["FunctionSpec"]
    if "ConversionSpec" in data:
        out["conversion_spec"] = data["ConversionSpec"]
    return out

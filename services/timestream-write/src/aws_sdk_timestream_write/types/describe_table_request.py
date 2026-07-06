"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.resource_name


class DescribeTableRequest(TypedDict, closed=True):
    database_name: "aws_sdk_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream database.</p>"""
    table_name: "aws_sdk_timestream_write.types.resource_name.ResourceName"
    """<p>The name of the Timestream table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTableRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTableRequest:
    out: DescribeTableRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("DescribeTableRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("DescribeTableRequest.table_name required")
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetLogFieldsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data_source_name
    import aws_sdk_cloudwatch_logs.types.data_source_type


class GetLogFieldsRequest(TypedDict):
    data_source_name: "aws_sdk_cloudwatch_logs.types.data_source_name.DataSourceName"
    """<p>The name of the data source to retrieve log fields for.</p>"""
    data_source_type: "aws_sdk_cloudwatch_logs.types.data_source_type.DataSourceType"
    """<p>The type of the data source to retrieve log fields for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLogFieldsRequest) -> dict:
    out: dict = {}
    out["dataSourceName"] = value["data_source_name"]
    out["dataSourceType"] = value["data_source_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLogFieldsRequest:
    out: GetLogFieldsRequest = {}  # type: ignore[typeddict-item]
    if "dataSourceName" in data:
        out["data_source_name"] = data["dataSourceName"]
    else:
        raise DeserializationError("GetLogFieldsRequest.data_source_name required")
    if "dataSourceType" in data:
        out["data_source_type"] = data["dataSourceType"]
    else:
        raise DeserializationError("GetLogFieldsRequest.data_source_type required")
    return out

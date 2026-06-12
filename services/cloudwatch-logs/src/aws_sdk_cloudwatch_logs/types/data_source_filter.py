"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataSourceFilter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data_source_name
    import aws_sdk_cloudwatch_logs.types.data_source_type


class DataSourceFilter(TypedDict):
    name: "aws_sdk_cloudwatch_logs.types.data_source_name.DataSourceName"
    """<p>The name pattern to filter data sources by.</p>"""
    type: NotRequired["aws_sdk_cloudwatch_logs.types.data_source_type.DataSourceType"]
    """<p>The type pattern to filter data sources by.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSourceFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSourceFilter:
    out: DataSourceFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataSourceFilter.name required")
    if "type" in data:
        out["type"] = data["type"]
    return out

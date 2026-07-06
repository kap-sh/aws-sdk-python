"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data_source_name
    import aws_sdk_cloudwatch_logs.types.data_source_type


class DataSource(TypedDict, closed=True):
    name: "aws_sdk_cloudwatch_logs.types.data_source_name.DataSourceName"
    """<p>The name of the data source.</p>"""
    type: NotRequired["aws_sdk_cloudwatch_logs.types.data_source_type.DataSourceType"]
    """<p>The type of the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DataSource.name required")
    if "type" in data:
        out["type"] = data["type"]
    return out

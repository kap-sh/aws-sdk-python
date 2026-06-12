"""Generated from Smithy shape ``com.amazonaws.timestreamquery#TimestreamDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.resource_name


class TimestreamDestination(TypedDict):
    database_name: NotRequired[
        "aws_sdk_timestream_query.types.resource_name.ResourceName"
    ]
    """<p>Timestream database name. </p>"""
    table_name: NotRequired["aws_sdk_timestream_query.types.resource_name.ResourceName"]
    """<p>Timestream table name. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamDestination) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamDestination:
    out: TimestreamDestination = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    return out

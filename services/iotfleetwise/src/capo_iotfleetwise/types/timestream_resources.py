"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimestreamResources``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.timestream_database_name
    import capo_iotfleetwise.types.timestream_table_name


class TimestreamResources(TypedDict, closed=True):
    timestream_database_name: (
        "capo_iotfleetwise.types.timestream_database_name.TimestreamDatabaseName"
    )
    """<p>The name of the registered Amazon Timestream database.</p>"""
    timestream_table_name: (
        "capo_iotfleetwise.types.timestream_table_name.TimestreamTableName"
    )
    """<p>The name of the registered Amazon Timestream database table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimestreamResources) -> dict:
    out: dict = {}
    out["timestreamDatabaseName"] = value["timestream_database_name"]
    out["timestreamTableName"] = value["timestream_table_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimestreamResources:
    out: TimestreamResources = {}  # type: ignore[typeddict-item]
    if "timestreamDatabaseName" in data:
        out["timestream_database_name"] = data["timestreamDatabaseName"]
    else:
        raise DeserializationError(
            "TimestreamResources.timestream_database_name required"
        )
    if "timestreamTableName" in data:
        out["timestream_table_name"] = data["timestreamTableName"]
    else:
        raise DeserializationError("TimestreamResources.timestream_table_name required")
    return out

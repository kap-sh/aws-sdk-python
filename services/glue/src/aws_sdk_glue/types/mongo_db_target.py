"""Generated from Smithy shape ``com.amazonaws.glue#MongoDBTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_name
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.path


class MongoDBTarget(TypedDict):
    connection_name: NotRequired["aws_sdk_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.</p>"""
    path: NotRequired["aws_sdk_glue.types.path.Path"]
    """<p>The path of the Amazon DocumentDB or MongoDB target (database/collection).</p>"""
    scan_all: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.</p> <p>A value of <code>true</code> means to scan all records, while a value of <code>false</code> means to sample the records. If no value is specified, the value defaults to <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MongoDBTarget) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "scan_all" in value:
        out["ScanAll"] = value["scan_all"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MongoDBTarget:
    out: MongoDBTarget = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "ScanAll" in data:
        out["scan_all"] = data["ScanAll"]
    return out

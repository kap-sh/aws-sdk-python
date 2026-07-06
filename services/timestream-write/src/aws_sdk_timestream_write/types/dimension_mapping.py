"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DimensionMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.schema_name


class DimensionMapping(TypedDict, closed=True):
    source_column: NotRequired["aws_sdk_timestream_write.types.schema_name.SchemaName"]
    """<p></p>"""
    destination_column: NotRequired[
        "aws_sdk_timestream_write.types.schema_name.SchemaName"
    ]
    """<p> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionMapping) -> dict:
    out: dict = {}
    if "source_column" in value:
        out["SourceColumn"] = value["source_column"]
    if "destination_column" in value:
        out["DestinationColumn"] = value["destination_column"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DimensionMapping:
    out: DimensionMapping = {}  # type: ignore[typeddict-item]
    if "SourceColumn" in data:
        out["source_column"] = data["SourceColumn"]
    if "DestinationColumn" in data:
        out["destination_column"] = data["DestinationColumn"]
    return out

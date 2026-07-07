"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#JSONMappingParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.record_row_path


class JSONMappingParameters(TypedDict, closed=True):
    record_row_path: "aws_sdk_kinesis_analytics.types.record_row_path.RecordRowPath"
    """<p>Path to the top-level parent that contains the records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JSONMappingParameters) -> dict:
    out: dict = {}
    out["RecordRowPath"] = value["record_row_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JSONMappingParameters:
    out: JSONMappingParameters = {}  # type: ignore[typeddict-item]
    if "RecordRowPath" in data:
        out["record_row_path"] = data["RecordRowPath"]
    else:
        raise DeserializationError("JSONMappingParameters.record_row_path required")
    return out

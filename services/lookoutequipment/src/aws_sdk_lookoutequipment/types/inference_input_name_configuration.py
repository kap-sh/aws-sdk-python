"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceInputNameConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.component_timestamp_delimiter
    import aws_sdk_lookoutequipment.types.file_name_timestamp_format


class InferenceInputNameConfiguration(TypedDict, closed=True):
    timestamp_format: NotRequired[
        "aws_sdk_lookoutequipment.types.file_name_timestamp_format.FileNameTimestampFormat"
    ]
    """<p>The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-). </p>"""
    component_timestamp_delimiter: NotRequired[
        "aws_sdk_lookoutequipment.types.component_timestamp_delimiter.ComponentTimestampDelimiter"
    ]
    """<p>Indicates the delimiter character used between items in the data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceInputNameConfiguration) -> dict:
    out: dict = {}
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    if "component_timestamp_delimiter" in value:
        out["ComponentTimestampDelimiter"] = value["component_timestamp_delimiter"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InferenceInputNameConfiguration:
    out: InferenceInputNameConfiguration = {}  # type: ignore[typeddict-item]
    if "TimestampFormat" in data:
        out["timestamp_format"] = data["TimestampFormat"]
    if "ComponentTimestampDelimiter" in data:
        out["component_timestamp_delimiter"] = data["ComponentTimestampDelimiter"]
    return out

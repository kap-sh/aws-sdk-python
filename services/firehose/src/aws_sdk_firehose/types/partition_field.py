"""Generated from Smithy shape ``com.amazonaws.firehose#PartitionField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.non_empty_string_without_whitespace


class PartitionField(TypedDict):
    source_name: "aws_sdk_firehose.types.non_empty_string_without_whitespace.NonEmptyStringWithoutWhitespace"
    """<p> The column name to be configured in partition spec. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartitionField) -> dict:
    out: dict = {}
    out["SourceName"] = value["source_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartitionField:
    out: PartitionField = {}  # type: ignore[typeddict-item]
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    else:
        raise DeserializationError("PartitionField.source_name required")
    return out

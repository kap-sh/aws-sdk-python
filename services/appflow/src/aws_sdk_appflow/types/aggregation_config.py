"""Generated from Smithy shape ``com.amazonaws.appflow#AggregationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.aggregation_type
    import aws_sdk_appflow.types.long


class AggregationConfig(TypedDict):
    aggregation_type: NotRequired[
        "aws_sdk_appflow.types.aggregation_type.AggregationType"
    ]
    """<p> Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated. </p>"""
    target_file_size: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p>The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationConfig) -> dict:
    out: dict = {}
    if "aggregation_type" in value:
        import aws_sdk_appflow.types.aggregation_type

        out["aggregationType"] = aws_sdk_appflow.types.aggregation_type.serialize_json(
            value["aggregation_type"]
        )
    if "target_file_size" in value:
        out["targetFileSize"] = value["target_file_size"]
    return out


def deserialize_json(data: dict) -> AggregationConfig:
    out: AggregationConfig = {}  # type: ignore[typeddict-item]
    if "aggregationType" in data:
        import aws_sdk_appflow.types.aggregation_type

        out["aggregation_type"] = (
            aws_sdk_appflow.types.aggregation_type.deserialize_json(
                data["aggregationType"]
            )
        )
    if "targetFileSize" in data:
        out["target_file_size"] = data["targetFileSize"]
    return out

"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamNameCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.comparison_operator
    import aws_sdk_kinesis_video.types.stream_name


class StreamNameCondition(TypedDict):
    comparison_operator: NotRequired[
        "aws_sdk_kinesis_video.types.comparison_operator.ComparisonOperator"
    ]
    """<p>A comparison operator. Currently, you can specify only the <code>BEGINS_WITH</code> operator, which finds streams whose names start with a given prefix.</p>"""
    comparison_value: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>A value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamNameCondition) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import aws_sdk_kinesis_video.types.comparison_operator

        out["ComparisonOperator"] = (
            aws_sdk_kinesis_video.types.comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "comparison_value" in value:
        out["ComparisonValue"] = value["comparison_value"]
    return out


def deserialize_json(data: dict) -> StreamNameCondition:
    out: StreamNameCondition = {}  # type: ignore[typeddict-item]
    if "ComparisonOperator" in data:
        import aws_sdk_kinesis_video.types.comparison_operator

        out["comparison_operator"] = (
            aws_sdk_kinesis_video.types.comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    if "ComparisonValue" in data:
        out["comparison_value"] = data["ComparisonValue"]
    return out

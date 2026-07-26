"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelNameCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.channel_name
    import capo_kinesis_video.types.comparison_operator


class ChannelNameCondition(TypedDict, closed=True):
    comparison_operator: NotRequired[
        "capo_kinesis_video.types.comparison_operator.ComparisonOperator"
    ]
    """<p>A comparison operator. Currently, you can only specify the <code>BEGINS_WITH</code> operator, which finds signaling channels whose names begin with a given prefix.</p>"""
    comparison_value: NotRequired["capo_kinesis_video.types.channel_name.ChannelName"]
    """<p>A value to compare.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelNameCondition) -> dict:
    out: dict = {}
    if "comparison_operator" in value:
        import capo_kinesis_video.types.comparison_operator

        out["ComparisonOperator"] = (
            capo_kinesis_video.types.comparison_operator.serialize_json(
                value["comparison_operator"]
            )
        )
    if "comparison_value" in value:
        out["ComparisonValue"] = value["comparison_value"]
    return out


def deserialize_json(data: dict) -> ChannelNameCondition:
    out: ChannelNameCondition = {}  # type: ignore[typeddict-item]
    if "ComparisonOperator" in data:
        import capo_kinesis_video.types.comparison_operator

        out["comparison_operator"] = (
            capo_kinesis_video.types.comparison_operator.deserialize_json(
                data["ComparisonOperator"]
            )
        )
    if "ComparisonValue" in data:
        out["comparison_value"] = data["ComparisonValue"]
    return out

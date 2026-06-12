"""Generated from Smithy shape ``com.amazonaws.xray#ProbabilisticRuleValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_double


class ProbabilisticRuleValue(TypedDict):
    desired_sampling_percentage: "aws_sdk_xray.types.nullable_double.NullableDouble"
    """<p> Configured sampling percentage of traceIds. Note that sampling can be subject to limits to ensure completeness of data. </p>"""
    actual_sampling_percentage: NotRequired[
        "aws_sdk_xray.types.nullable_double.NullableDouble"
    ]
    """<p> Applied sampling percentage of traceIds. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbabilisticRuleValue) -> dict:
    out: dict = {}
    out["DesiredSamplingPercentage"] = value["desired_sampling_percentage"]
    if "actual_sampling_percentage" in value:
        out["ActualSamplingPercentage"] = value["actual_sampling_percentage"]
    return out


def deserialize_json(data: dict) -> ProbabilisticRuleValue:
    out: ProbabilisticRuleValue = {}  # type: ignore[typeddict-item]
    if "DesiredSamplingPercentage" in data:
        out["desired_sampling_percentage"] = data["DesiredSamplingPercentage"]
    else:
        raise DeserializationError(
            "ProbabilisticRuleValue.desired_sampling_percentage required"
        )
    if "ActualSamplingPercentage" in data:
        out["actual_sampling_percentage"] = data["ActualSamplingPercentage"]
    return out

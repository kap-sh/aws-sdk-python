"""Generated from Smithy shape ``com.amazonaws.xray#ProbabilisticRuleValueUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.nullable_double


class ProbabilisticRuleValueUpdate(TypedDict, closed=True):
    desired_sampling_percentage: "aws_sdk_xray.types.nullable_double.NullableDouble"
    """<p> Configured sampling percentage of traceIds. Note that sampling can be subject to limits to ensure completeness of data. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbabilisticRuleValueUpdate) -> dict:
    out: dict = {}
    out["DesiredSamplingPercentage"] = value["desired_sampling_percentage"]
    return out


def deserialize_json(data: dict) -> ProbabilisticRuleValueUpdate:
    out: ProbabilisticRuleValueUpdate = {}  # type: ignore[typeddict-item]
    if "DesiredSamplingPercentage" in data:
        out["desired_sampling_percentage"] = data["DesiredSamplingPercentage"]
    else:
        raise DeserializationError(
            "ProbabilisticRuleValueUpdate.desired_sampling_percentage required"
        )
    return out

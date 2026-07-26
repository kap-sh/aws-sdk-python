"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContinuousParameterRangeSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parameter_value


class ContinuousParameterRangeSpecification(TypedDict, closed=True):
    min_value: NotRequired["capo_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The minimum floating-point value allowed.</p>"""
    max_value: NotRequired["capo_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The maximum floating-point value allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousParameterRangeSpecification) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinuousParameterRangeSpecification:
    out: ContinuousParameterRangeSpecification = {}  # type: ignore[typeddict-item]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#IntegerParameterRangeSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter_value


class IntegerParameterRangeSpecification(TypedDict):
    min_value: NotRequired["aws_sdk_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The minimum integer value allowed.</p>"""
    max_value: NotRequired["aws_sdk_sagemaker.types.parameter_value.ParameterValue"]
    """<p>The maximum integer value allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerParameterRangeSpecification) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IntegerParameterRangeSpecification:
    out: IntegerParameterRangeSpecification = {}  # type: ignore[typeddict-item]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    return out

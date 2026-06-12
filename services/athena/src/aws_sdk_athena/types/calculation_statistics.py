"""Generated from Smithy shape ``com.amazonaws.athena#CalculationStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.description_string
    import aws_sdk_athena.types.long


class CalculationStatistics(TypedDict):
    dpu_execution_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The data processing unit execution time in milliseconds for the calculation.</p>"""
    progress: NotRequired["aws_sdk_athena.types.description_string.DescriptionString"]
    """<p>The progress of the calculation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationStatistics) -> dict:
    out: dict = {}
    if "dpu_execution_in_millis" in value:
        out["DpuExecutionInMillis"] = value["dpu_execution_in_millis"]
    if "progress" in value:
        out["Progress"] = value["progress"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculationStatistics:
    out: CalculationStatistics = {}  # type: ignore[typeddict-item]
    if "DpuExecutionInMillis" in data:
        out["dpu_execution_in_millis"] = data["DpuExecutionInMillis"]
    if "Progress" in data:
        out["progress"] = data["Progress"]
    return out

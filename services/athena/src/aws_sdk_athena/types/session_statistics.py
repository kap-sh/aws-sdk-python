"""Generated from Smithy shape ``com.amazonaws.athena#SessionStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.long


class SessionStatistics(TypedDict, closed=True):
    dpu_execution_in_millis: NotRequired["aws_sdk_athena.types.long.Long"]
    """<p>The data processing unit execution time for a session in milliseconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionStatistics) -> dict:
    out: dict = {}
    if "dpu_execution_in_millis" in value:
        out["DpuExecutionInMillis"] = value["dpu_execution_in_millis"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SessionStatistics:
    out: SessionStatistics = {}  # type: ignore[typeddict-item]
    if "DpuExecutionInMillis" in data:
        out["dpu_execution_in_millis"] = data["DpuExecutionInMillis"]
    return out

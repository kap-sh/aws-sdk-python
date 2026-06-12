"""Generated from Smithy shape ``com.amazonaws.athena#StopCalculationExecutionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_execution_id


class StopCalculationExecutionRequest(TypedDict):
    calculation_execution_id: (
        "aws_sdk_athena.types.calculation_execution_id.CalculationExecutionId"
    )
    """<p>The calculation execution UUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCalculationExecutionRequest) -> dict:
    out: dict = {}
    out["CalculationExecutionId"] = value["calculation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCalculationExecutionRequest:
    out: StopCalculationExecutionRequest = {}  # type: ignore[typeddict-item]
    if "CalculationExecutionId" in data:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    else:
        raise DeserializationError(
            "StopCalculationExecutionRequest.calculation_execution_id required"
        )
    return out

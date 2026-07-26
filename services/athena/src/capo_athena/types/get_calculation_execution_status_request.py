"""Generated from Smithy shape ``com.amazonaws.athena#GetCalculationExecutionStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.calculation_execution_id


class GetCalculationExecutionStatusRequest(TypedDict, closed=True):
    calculation_execution_id: (
        "capo_athena.types.calculation_execution_id.CalculationExecutionId"
    )
    """<p>The calculation execution UUID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalculationExecutionStatusRequest) -> dict:
    out: dict = {}
    out["CalculationExecutionId"] = value["calculation_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalculationExecutionStatusRequest:
    out: GetCalculationExecutionStatusRequest = {}  # type: ignore[typeddict-item]
    if "CalculationExecutionId" in data:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    else:
        raise DeserializationError(
            "GetCalculationExecutionStatusRequest.calculation_execution_id required"
        )
    return out

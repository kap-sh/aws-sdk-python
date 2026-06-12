"""Generated from Smithy shape ``com.amazonaws.athena#StartCalculationExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.calculation_execution_id
    import aws_sdk_athena.types.calculation_execution_state


class StartCalculationExecutionResponse(TypedDict):
    calculation_execution_id: NotRequired[
        "aws_sdk_athena.types.calculation_execution_id.CalculationExecutionId"
    ]
    """<p>The calculation execution UUID.</p>"""
    state: NotRequired[
        "aws_sdk_athena.types.calculation_execution_state.CalculationExecutionState"
    ]
    """<p> <code>CREATING</code> - The calculation is in the process of being created.</p> <p> <code>CREATED</code> - The calculation has been created and is ready to run.</p> <p> <code>QUEUED</code> - The calculation has been queued for processing.</p> <p> <code>RUNNING</code> - The calculation is running.</p> <p> <code>CANCELING</code> - A request to cancel the calculation has been received and the system is working to stop it.</p> <p> <code>CANCELED</code> - The calculation is no longer running as the result of a cancel request.</p> <p> <code>COMPLETED</code> - The calculation has completed without error.</p> <p> <code>FAILED</code> - The calculation failed and is no longer running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCalculationExecutionResponse) -> dict:
    out: dict = {}
    if "calculation_execution_id" in value:
        out["CalculationExecutionId"] = value["calculation_execution_id"]
    if "state" in value:
        import aws_sdk_athena.types.calculation_execution_state

        out["State"] = (
            aws_sdk_athena.types.calculation_execution_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCalculationExecutionResponse:
    out: StartCalculationExecutionResponse = {}  # type: ignore[typeddict-item]
    if "CalculationExecutionId" in data:
        out["calculation_execution_id"] = data["CalculationExecutionId"]
    if "State" in data:
        import aws_sdk_athena.types.calculation_execution_state

        out["state"] = (
            aws_sdk_athena.types.calculation_execution_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.athena#StopCalculationExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_execution_state


class StopCalculationExecutionResponse(TypedDict, closed=True):
    state: NotRequired[
        "capo_athena.types.calculation_execution_state.CalculationExecutionState"
    ]
    """<p> <code>CREATING</code> - The calculation is in the process of being created.</p> <p> <code>CREATED</code> - The calculation has been created and is ready to run.</p> <p> <code>QUEUED</code> - The calculation has been queued for processing.</p> <p> <code>RUNNING</code> - The calculation is running.</p> <p> <code>CANCELING</code> - A request to cancel the calculation has been received and the system is working to stop it.</p> <p> <code>CANCELED</code> - The calculation is no longer running as the result of a cancel request.</p> <p> <code>COMPLETED</code> - The calculation has completed without error.</p> <p> <code>FAILED</code> - The calculation failed and is no longer running.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCalculationExecutionResponse) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_athena.types.calculation_execution_state

        out["State"] = (
            capo_athena.types.calculation_execution_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCalculationExecutionResponse:
    out: StopCalculationExecutionResponse = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_athena.types.calculation_execution_state

        out["state"] = (
            capo_athena.types.calculation_execution_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out

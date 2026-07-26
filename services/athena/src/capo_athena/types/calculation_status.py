"""Generated from Smithy shape ``com.amazonaws.athena#CalculationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_execution_state
    import capo_athena.types.date
    import capo_athena.types.description_string


class CalculationStatus(TypedDict, closed=True):
    submission_date_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The date and time the calculation was submitted for processing.</p>"""
    completion_date_time: NotRequired["capo_athena.types.date.Date"]
    """<p>The date and time the calculation completed processing.</p>"""
    state: NotRequired[
        "capo_athena.types.calculation_execution_state.CalculationExecutionState"
    ]
    """<p>The state of the calculation execution. A description of each state follows.</p> <p> <code>CREATING</code> - The calculation is in the process of being created.</p> <p> <code>CREATED</code> - The calculation has been created and is ready to run.</p> <p> <code>QUEUED</code> - The calculation has been queued for processing.</p> <p> <code>RUNNING</code> - The calculation is running.</p> <p> <code>CANCELING</code> - A request to cancel the calculation has been received and the system is working to stop it.</p> <p> <code>CANCELED</code> - The calculation is no longer running as the result of a cancel request.</p> <p> <code>COMPLETED</code> - The calculation has completed without error.</p> <p> <code>FAILED</code> - The calculation failed and is no longer running.</p>"""
    state_change_reason: NotRequired[
        "capo_athena.types.description_string.DescriptionString"
    ]
    """<p>The reason for the calculation state change (for example, the calculation was canceled because the session was terminated).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CalculationStatus) -> dict:
    out: dict = {}
    if "submission_date_time" in value:
        import capo_athena.types.date

        out["SubmissionDateTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["submission_date_time"]
        )
    if "completion_date_time" in value:
        import capo_athena.types.date

        out["CompletionDateTime"] = capo_athena.types.date.serialize_aws_json_1_1(
            value["completion_date_time"]
        )
    if "state" in value:
        import capo_athena.types.calculation_execution_state

        out["State"] = (
            capo_athena.types.calculation_execution_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_change_reason" in value:
        out["StateChangeReason"] = value["state_change_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CalculationStatus:
    out: CalculationStatus = {}  # type: ignore[typeddict-item]
    if "SubmissionDateTime" in data:
        import capo_athena.types.date

        out["submission_date_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["SubmissionDateTime"]
        )
    if "CompletionDateTime" in data:
        import capo_athena.types.date

        out["completion_date_time"] = capo_athena.types.date.deserialize_aws_json_1_1(
            data["CompletionDateTime"]
        )
    if "State" in data:
        import capo_athena.types.calculation_execution_state

        out["state"] = (
            capo_athena.types.calculation_execution_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateChangeReason" in data:
        out["state_change_reason"] = data["StateChangeReason"]
    return out

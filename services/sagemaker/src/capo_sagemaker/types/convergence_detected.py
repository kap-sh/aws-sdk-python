"""Generated from Smithy shape ``com.amazonaws.sagemaker#ConvergenceDetected``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.complete_on_convergence


class ConvergenceDetected(TypedDict, closed=True):
    complete_on_convergence: NotRequired[
        "capo_sagemaker.types.complete_on_convergence.CompleteOnConvergence"
    ]
    """<p>A flag to stop a tuning job once AMT has detected that the job has converged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConvergenceDetected) -> dict:
    out: dict = {}
    if "complete_on_convergence" in value:
        import capo_sagemaker.types.complete_on_convergence

        out["CompleteOnConvergence"] = (
            capo_sagemaker.types.complete_on_convergence.serialize_aws_json_1_1(
                value["complete_on_convergence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConvergenceDetected:
    out: ConvergenceDetected = {}  # type: ignore[typeddict-item]
    if "CompleteOnConvergence" in data:
        import capo_sagemaker.types.complete_on_convergence

        out["complete_on_convergence"] = (
            capo_sagemaker.types.complete_on_convergence.deserialize_aws_json_1_1(
                data["CompleteOnConvergence"]
            )
        )
    return out

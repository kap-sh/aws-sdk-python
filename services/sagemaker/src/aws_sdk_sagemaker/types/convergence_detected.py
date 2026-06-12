"""Generated from Smithy shape ``com.amazonaws.sagemaker#ConvergenceDetected``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.complete_on_convergence


class ConvergenceDetected(TypedDict):
    complete_on_convergence: NotRequired[
        "aws_sdk_sagemaker.types.complete_on_convergence.CompleteOnConvergence"
    ]
    """<p>A flag to stop a tuning job once AMT has detected that the job has converged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConvergenceDetected) -> dict:
    out: dict = {}
    if "complete_on_convergence" in value:
        import aws_sdk_sagemaker.types.complete_on_convergence

        out["CompleteOnConvergence"] = (
            aws_sdk_sagemaker.types.complete_on_convergence.serialize_aws_json_1_1(
                value["complete_on_convergence"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConvergenceDetected:
    out: ConvergenceDetected = {}  # type: ignore[typeddict-item]
    if "CompleteOnConvergence" in data:
        import aws_sdk_sagemaker.types.complete_on_convergence

        out["complete_on_convergence"] = (
            aws_sdk_sagemaker.types.complete_on_convergence.deserialize_aws_json_1_1(
                data["CompleteOnConvergence"]
            )
        )
    return out

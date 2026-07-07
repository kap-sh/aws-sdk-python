"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaSavingsEstimationMode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source


class LambdaSavingsEstimationMode(TypedDict, closed=True):
    source: NotRequired[
        "aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source.LambdaSavingsEstimationModeSource"
    ]
    """<p> Describes the source for calculation of savings opportunity for Lambda functions. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaSavingsEstimationMode) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaSavingsEstimationMode:
    out: LambdaSavingsEstimationMode = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.lambda_savings_estimation_mode_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    return out

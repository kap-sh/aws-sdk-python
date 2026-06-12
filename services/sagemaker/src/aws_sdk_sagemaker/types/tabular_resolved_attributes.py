"""Generated from Smithy shape ``com.amazonaws.sagemaker#TabularResolvedAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.problem_type


class TabularResolvedAttributes(TypedDict):
    problem_type: NotRequired["aws_sdk_sagemaker.types.problem_type.ProblemType"]
    """<p>The type of supervised learning problem available for the model candidates of the AutoML job V2 (Binary Classification, Multiclass Classification, Regression). For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types\"> SageMaker Autopilot problem types</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TabularResolvedAttributes) -> dict:
    out: dict = {}
    if "problem_type" in value:
        import aws_sdk_sagemaker.types.problem_type

        out["ProblemType"] = (
            aws_sdk_sagemaker.types.problem_type.serialize_aws_json_1_1(
                value["problem_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TabularResolvedAttributes:
    out: TabularResolvedAttributes = {}  # type: ignore[typeddict-item]
    if "ProblemType" in data:
        import aws_sdk_sagemaker.types.problem_type

        out["problem_type"] = (
            aws_sdk_sagemaker.types.problem_type.deserialize_aws_json_1_1(
                data["ProblemType"]
            )
        )
    return out

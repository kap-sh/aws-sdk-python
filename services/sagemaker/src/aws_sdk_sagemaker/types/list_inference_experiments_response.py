"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceExperimentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_experiment_list
    import aws_sdk_sagemaker.types.next_token


class ListInferenceExperimentsResponse(TypedDict, closed=True):
    inference_experiments: NotRequired[
        "aws_sdk_sagemaker.types.inference_experiment_list.InferenceExperimentList"
    ]
    """<p>List of inference experiments.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>The token to use when calling the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceExperimentsResponse) -> dict:
    out: dict = {}
    if "inference_experiments" in value:
        import aws_sdk_sagemaker.types.inference_experiment_list

        out["InferenceExperiments"] = (
            aws_sdk_sagemaker.types.inference_experiment_list.serialize_aws_json_1_1(
                value["inference_experiments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceExperimentsResponse:
    out: ListInferenceExperimentsResponse = {}  # type: ignore[typeddict-item]
    if "InferenceExperiments" in data:
        import aws_sdk_sagemaker.types.inference_experiment_list

        out["inference_experiments"] = (
            aws_sdk_sagemaker.types.inference_experiment_list.deserialize_aws_json_1_1(
                data["InferenceExperiments"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

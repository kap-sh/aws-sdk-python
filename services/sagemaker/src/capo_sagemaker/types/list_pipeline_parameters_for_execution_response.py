"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListPipelineParametersForExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.parameter_list


class ListPipelineParametersForExecutionResponse(TypedDict, closed=True):
    pipeline_parameters: NotRequired[
        "capo_sagemaker.types.parameter_list.ParameterList"
    ]
    """<p>Contains a list of pipeline parameters. This list can be empty. </p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListPipelineParametersForExecution</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of parameters, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineParametersForExecutionResponse) -> dict:
    out: dict = {}
    if "pipeline_parameters" in value:
        import capo_sagemaker.types.parameter_list

        out["PipelineParameters"] = (
            capo_sagemaker.types.parameter_list.serialize_aws_json_1_1(
                value["pipeline_parameters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineParametersForExecutionResponse:
    out: ListPipelineParametersForExecutionResponse = {}  # type: ignore[typeddict-item]
    if "PipelineParameters" in data:
        import capo_sagemaker.types.parameter_list

        out["pipeline_parameters"] = (
            capo_sagemaker.types.parameter_list.deserialize_aws_json_1_1(
                data["PipelineParameters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

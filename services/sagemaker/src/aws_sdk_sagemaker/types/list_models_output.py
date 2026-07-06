"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_summary_list
    import aws_sdk_sagemaker.types.pagination_token


class ListModelsOutput(TypedDict, closed=True):
    models: NotRequired["aws_sdk_sagemaker.types.model_summary_list.ModelSummaryList"]
    """<p>An array of <code>ModelSummary</code> objects, each of which lists a model.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.pagination_token.PaginationToken"]
    """<p> If the response is truncated, SageMaker returns this token. To retrieve the next set of models, use it in the subsequent request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelsOutput) -> dict:
    out: dict = {}
    if "models" in value:
        import aws_sdk_sagemaker.types.model_summary_list

        out["Models"] = (
            aws_sdk_sagemaker.types.model_summary_list.serialize_aws_json_1_1(
                value["models"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelsOutput:
    out: ListModelsOutput = {}  # type: ignore[typeddict-item]
    if "Models" in data:
        import aws_sdk_sagemaker.types.model_summary_list

        out["models"] = (
            aws_sdk_sagemaker.types.model_summary_list.deserialize_aws_json_1_1(
                data["Models"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

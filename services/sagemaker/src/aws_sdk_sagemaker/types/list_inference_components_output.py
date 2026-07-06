"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceComponentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_summary_list
    import aws_sdk_sagemaker.types.pagination_token


class ListInferenceComponentsOutput(TypedDict, closed=True):
    inference_components: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_summary_list.InferenceComponentSummaryList"
    ]
    """<p>A list of inference components and their properties that matches any of the filters you specified in the request.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.pagination_token.PaginationToken"]
    """<p>The token to use in a subsequent request to get the next set of results following a truncated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceComponentsOutput) -> dict:
    out: dict = {}
    if "inference_components" in value:
        import aws_sdk_sagemaker.types.inference_component_summary_list

        out["InferenceComponents"] = (
            aws_sdk_sagemaker.types.inference_component_summary_list.serialize_aws_json_1_1(
                value["inference_components"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListInferenceComponentsOutput:
    out: ListInferenceComponentsOutput = {}  # type: ignore[typeddict-item]
    if "InferenceComponents" in data:
        import aws_sdk_sagemaker.types.inference_component_summary_list

        out["inference_components"] = (
            aws_sdk_sagemaker.types.inference_component_summary_list.deserialize_aws_json_1_1(
                data["InferenceComponents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

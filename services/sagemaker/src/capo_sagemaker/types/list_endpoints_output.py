"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEndpointsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.endpoint_summary_list
    import capo_sagemaker.types.pagination_token


class ListEndpointsOutput(TypedDict, closed=True):
    endpoints: NotRequired[
        "capo_sagemaker.types.endpoint_summary_list.EndpointSummaryList"
    ]
    """<p> An array or endpoint objects. </p>"""
    next_token: NotRequired["capo_sagemaker.types.pagination_token.PaginationToken"]
    """<p> If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsOutput) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import capo_sagemaker.types.endpoint_summary_list

        out["Endpoints"] = (
            capo_sagemaker.types.endpoint_summary_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsOutput:
    out: ListEndpointsOutput = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import capo_sagemaker.types.endpoint_summary_list

        out["endpoints"] = (
            capo_sagemaker.types.endpoint_summary_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

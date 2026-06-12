"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEndpointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_summary_list
    import aws_sdk_sagemaker.types.pagination_token


class ListEndpointsOutput(TypedDict):
    endpoints: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_summary_list.EndpointSummaryList"
    ]
    """<p> An array or endpoint objects. </p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.pagination_token.PaginationToken"]
    """<p> If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsOutput) -> dict:
    out: dict = {}
    if "endpoints" in value:
        import aws_sdk_sagemaker.types.endpoint_summary_list

        out["Endpoints"] = (
            aws_sdk_sagemaker.types.endpoint_summary_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsOutput:
    out: ListEndpointsOutput = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_sagemaker.types.endpoint_summary_list

        out["endpoints"] = (
            aws_sdk_sagemaker.types.endpoint_summary_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListEndpointConfigsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_config_summary_list
    import aws_sdk_sagemaker.types.pagination_token


class ListEndpointConfigsOutput(TypedDict, closed=True):
    endpoint_configs: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_config_summary_list.EndpointConfigSummaryList"
    ]
    """<p>An array of endpoint configurations.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.pagination_token.PaginationToken"]
    """<p> If the response is truncated, SageMaker returns this token. To retrieve the next set of endpoint configurations, use it in the subsequent request </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointConfigsOutput) -> dict:
    out: dict = {}
    if "endpoint_configs" in value:
        import aws_sdk_sagemaker.types.endpoint_config_summary_list

        out["EndpointConfigs"] = (
            aws_sdk_sagemaker.types.endpoint_config_summary_list.serialize_aws_json_1_1(
                value["endpoint_configs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointConfigsOutput:
    out: ListEndpointConfigsOutput = {}  # type: ignore[typeddict-item]
    if "EndpointConfigs" in data:
        import aws_sdk_sagemaker.types.endpoint_config_summary_list

        out["endpoint_configs"] = (
            aws_sdk_sagemaker.types.endpoint_config_summary_list.deserialize_aws_json_1_1(
                data["EndpointConfigs"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListCloudConnectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.cloud_connector_type
    import aws_sdk_iot_managed_integrations.types.lambda_arn
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token


class ListCloudConnectorsRequest(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
    ]
    """<p>The type of cloud connectors to filter by when listing available connectors.</p>"""
    lambda_arn: NotRequired[
        "aws_sdk_iot_managed_integrations.types.lambda_arn.LambdaArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Lambda function to filter cloud connectors by.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCloudConnectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCloudConnectorsRequest:
    out: ListCloudConnectorsRequest = {}  # type: ignore[typeddict-item]
    return out

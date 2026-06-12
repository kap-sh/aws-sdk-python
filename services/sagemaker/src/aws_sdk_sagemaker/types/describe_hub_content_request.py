"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHubContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name_or_arn


class DescribeHubContentRequest(TypedDict):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub that contains the content to describe.</p>"""
    hub_content_type: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of content in the hub.</p>"""
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the content to describe.</p>"""
    hub_content_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The version of the content to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHubContentRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_type" in value:
        import aws_sdk_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            aws_sdk_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHubContentRequest:
    out: DescribeHubContentRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentType" in data:
        import aws_sdk_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            aws_sdk_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    return out

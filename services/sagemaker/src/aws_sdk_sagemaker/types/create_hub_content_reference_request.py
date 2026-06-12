"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHubContentReferenceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name_or_arn
    import aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateHubContentReferenceRequest(TypedDict):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to add the hub content reference to.</p>"""
    sage_maker_public_hub_content_arn: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_public_hub_content_arn.SageMakerPublicHubContentArn"
    ]
    """<p>The ARN of the public hub content to reference.</p>"""
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content to reference.</p>"""
    min_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The minimum version of the hub content to reference.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    """<p>Any tags associated with the hub content to reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHubContentReferenceRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "sage_maker_public_hub_content_arn" in value:
        out["SageMakerPublicHubContentArn"] = value["sage_maker_public_hub_content_arn"]
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "min_version" in value:
        out["MinVersion"] = value["min_version"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHubContentReferenceRequest:
    out: CreateHubContentReferenceRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "SageMakerPublicHubContentArn" in data:
        out["sage_maker_public_hub_content_arn"] = data["SageMakerPublicHubContentArn"]
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "MinVersion" in data:
        out["min_version"] = data["MinVersion"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

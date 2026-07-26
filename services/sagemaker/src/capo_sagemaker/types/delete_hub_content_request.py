"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteHubContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_content_name
    import capo_sagemaker.types.hub_content_type
    import capo_sagemaker.types.hub_content_version
    import capo_sagemaker.types.hub_name_or_arn


class DeleteHubContentRequest(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub that you want to delete content in.</p>"""
    hub_content_type: NotRequired[
        "capo_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of content that you want to delete from a hub.</p>"""
    hub_content_name: NotRequired[
        "capo_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the content that you want to delete from a hub.</p>"""
    hub_content_version: NotRequired[
        "capo_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The version of the content that you want to delete from a hub.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHubContentRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_type" in value:
        import capo_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            capo_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "hub_content_version" in value:
        out["HubContentVersion"] = value["hub_content_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHubContentRequest:
    out: DeleteHubContentRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentType" in data:
        import capo_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            capo_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "HubContentVersion" in data:
        out["hub_content_version"] = data["HubContentVersion"]
    return out

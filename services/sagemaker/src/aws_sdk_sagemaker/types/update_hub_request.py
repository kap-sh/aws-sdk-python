"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateHubRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_description
    import aws_sdk_sagemaker.types.hub_display_name
    import aws_sdk_sagemaker.types.hub_name_or_arn
    import aws_sdk_sagemaker.types.hub_search_keyword_list


class UpdateHubRequest(TypedDict):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to update.</p>"""
    hub_description: NotRequired[
        "aws_sdk_sagemaker.types.hub_description.HubDescription"
    ]
    """<p>A description of the updated hub.</p>"""
    hub_display_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_display_name.HubDisplayName"
    ]
    """<p>The display name of the hub.</p>"""
    hub_search_keywords: NotRequired[
        "aws_sdk_sagemaker.types.hub_search_keyword_list.HubSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHubRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_description" in value:
        out["HubDescription"] = value["hub_description"]
    if "hub_display_name" in value:
        out["HubDisplayName"] = value["hub_display_name"]
    if "hub_search_keywords" in value:
        import aws_sdk_sagemaker.types.hub_search_keyword_list

        out["HubSearchKeywords"] = (
            aws_sdk_sagemaker.types.hub_search_keyword_list.serialize_aws_json_1_1(
                value["hub_search_keywords"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHubRequest:
    out: UpdateHubRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubDescription" in data:
        out["hub_description"] = data["HubDescription"]
    if "HubDisplayName" in data:
        out["hub_display_name"] = data["HubDisplayName"]
    if "HubSearchKeywords" in data:
        import aws_sdk_sagemaker.types.hub_search_keyword_list

        out["hub_search_keywords"] = (
            aws_sdk_sagemaker.types.hub_search_keyword_list.deserialize_aws_json_1_1(
                data["HubSearchKeywords"]
            )
        )
    return out

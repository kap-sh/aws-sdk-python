"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateHubRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hub_description
    import capo_sagemaker.types.hub_display_name
    import capo_sagemaker.types.hub_name
    import capo_sagemaker.types.hub_s3_storage_config
    import capo_sagemaker.types.hub_search_keyword_list
    import capo_sagemaker.types.tag_list


class CreateHubRequest(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name.HubName"]
    """<p>The name of the hub to create.</p>"""
    hub_description: NotRequired["capo_sagemaker.types.hub_description.HubDescription"]
    """<p>A description of the hub.</p>"""
    hub_display_name: NotRequired[
        "capo_sagemaker.types.hub_display_name.HubDisplayName"
    ]
    """<p>The display name of the hub.</p>"""
    hub_search_keywords: NotRequired[
        "capo_sagemaker.types.hub_search_keyword_list.HubSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub.</p>"""
    s3_storage_config: NotRequired[
        "capo_sagemaker.types.hub_s3_storage_config.HubS3StorageConfig"
    ]
    """<p>The Amazon S3 storage configuration for the hub.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Any tags to associate with the hub.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHubRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_description" in value:
        out["HubDescription"] = value["hub_description"]
    if "hub_display_name" in value:
        out["HubDisplayName"] = value["hub_display_name"]
    if "hub_search_keywords" in value:
        import capo_sagemaker.types.hub_search_keyword_list

        out["HubSearchKeywords"] = (
            capo_sagemaker.types.hub_search_keyword_list.serialize_aws_json_1_1(
                value["hub_search_keywords"]
            )
        )
    if "s3_storage_config" in value:
        import capo_sagemaker.types.hub_s3_storage_config

        out["S3StorageConfig"] = (
            capo_sagemaker.types.hub_s3_storage_config.serialize_aws_json_1_1(
                value["s3_storage_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHubRequest:
    out: CreateHubRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubDescription" in data:
        out["hub_description"] = data["HubDescription"]
    if "HubDisplayName" in data:
        out["hub_display_name"] = data["HubDisplayName"]
    if "HubSearchKeywords" in data:
        import capo_sagemaker.types.hub_search_keyword_list

        out["hub_search_keywords"] = (
            capo_sagemaker.types.hub_search_keyword_list.deserialize_aws_json_1_1(
                data["HubSearchKeywords"]
            )
        )
    if "S3StorageConfig" in data:
        import capo_sagemaker.types.hub_s3_storage_config

        out["s3_storage_config"] = (
            capo_sagemaker.types.hub_s3_storage_config.deserialize_aws_json_1_1(
                data["S3StorageConfig"]
            )
        )
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out

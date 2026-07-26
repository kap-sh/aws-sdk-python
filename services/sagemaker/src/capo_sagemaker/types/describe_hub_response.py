"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeHubResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.hub_arn
    import capo_sagemaker.types.hub_description
    import capo_sagemaker.types.hub_display_name
    import capo_sagemaker.types.hub_name
    import capo_sagemaker.types.hub_s3_storage_config
    import capo_sagemaker.types.hub_search_keyword_list
    import capo_sagemaker.types.hub_status
    import capo_sagemaker.types.timestamp


class DescribeHubResponse(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name.HubName"]
    """<p>The name of the hub.</p>"""
    hub_arn: NotRequired["capo_sagemaker.types.hub_arn.HubArn"]
    """<p>The Amazon Resource Name (ARN) of the hub.</p>"""
    hub_display_name: NotRequired[
        "capo_sagemaker.types.hub_display_name.HubDisplayName"
    ]
    """<p>The display name of the hub.</p>"""
    hub_description: NotRequired["capo_sagemaker.types.hub_description.HubDescription"]
    """<p>A description of the hub.</p>"""
    hub_search_keywords: NotRequired[
        "capo_sagemaker.types.hub_search_keyword_list.HubSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub.</p>"""
    s3_storage_config: NotRequired[
        "capo_sagemaker.types.hub_s3_storage_config.HubS3StorageConfig"
    ]
    """<p>The Amazon S3 storage configuration for the hub.</p>"""
    hub_status: NotRequired["capo_sagemaker.types.hub_status.HubStatus"]
    """<p>The status of the hub.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason if importing hub content failed.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the hub was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the hub was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHubResponse) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_arn" in value:
        out["HubArn"] = value["hub_arn"]
    if "hub_display_name" in value:
        out["HubDisplayName"] = value["hub_display_name"]
    if "hub_description" in value:
        out["HubDescription"] = value["hub_description"]
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
    if "hub_status" in value:
        import capo_sagemaker.types.hub_status

        out["HubStatus"] = capo_sagemaker.types.hub_status.serialize_aws_json_1_1(
            value["hub_status"]
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHubResponse:
    out: DescribeHubResponse = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "HubDisplayName" in data:
        out["hub_display_name"] = data["HubDisplayName"]
    if "HubDescription" in data:
        out["hub_description"] = data["HubDescription"]
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
    if "HubStatus" in data:
        import capo_sagemaker.types.hub_status

        out["hub_status"] = capo_sagemaker.types.hub_status.deserialize_aws_json_1_1(
            data["HubStatus"]
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out

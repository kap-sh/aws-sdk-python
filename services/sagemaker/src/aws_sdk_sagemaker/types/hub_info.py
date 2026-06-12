"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hub_arn
    import aws_sdk_sagemaker.types.hub_description
    import aws_sdk_sagemaker.types.hub_display_name
    import aws_sdk_sagemaker.types.hub_name
    import aws_sdk_sagemaker.types.hub_search_keyword_list
    import aws_sdk_sagemaker.types.hub_status
    import aws_sdk_sagemaker.types.timestamp


class HubInfo(TypedDict):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name.HubName"]
    """<p>The name of the hub.</p>"""
    hub_arn: NotRequired["aws_sdk_sagemaker.types.hub_arn.HubArn"]
    """<p>The Amazon Resource Name (ARN) of the hub.</p>"""
    hub_display_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_display_name.HubDisplayName"
    ]
    """<p>The display name of the hub.</p>"""
    hub_description: NotRequired[
        "aws_sdk_sagemaker.types.hub_description.HubDescription"
    ]
    """<p>A description of the hub.</p>"""
    hub_search_keywords: NotRequired[
        "aws_sdk_sagemaker.types.hub_search_keyword_list.HubSearchKeywordList"
    ]
    """<p>The searchable keywords for the hub.</p>"""
    hub_status: NotRequired["aws_sdk_sagemaker.types.hub_status.HubStatus"]
    """<p>The status of the hub.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the hub was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the hub was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubInfo) -> dict:
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
        import aws_sdk_sagemaker.types.hub_search_keyword_list

        out["HubSearchKeywords"] = (
            aws_sdk_sagemaker.types.hub_search_keyword_list.serialize_aws_json_1_1(
                value["hub_search_keywords"]
            )
        )
    if "hub_status" in value:
        import aws_sdk_sagemaker.types.hub_status

        out["HubStatus"] = aws_sdk_sagemaker.types.hub_status.serialize_aws_json_1_1(
            value["hub_status"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HubInfo:
    out: HubInfo = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubArn" in data:
        out["hub_arn"] = data["HubArn"]
    if "HubDisplayName" in data:
        out["hub_display_name"] = data["HubDisplayName"]
    if "HubDescription" in data:
        out["hub_description"] = data["HubDescription"]
    if "HubSearchKeywords" in data:
        import aws_sdk_sagemaker.types.hub_search_keyword_list

        out["hub_search_keywords"] = (
            aws_sdk_sagemaker.types.hub_search_keyword_list.deserialize_aws_json_1_1(
                data["HubSearchKeywords"]
            )
        )
    if "HubStatus" in data:
        import aws_sdk_sagemaker.types.hub_status

        out["hub_status"] = aws_sdk_sagemaker.types.hub_status.deserialize_aws_json_1_1(
            data["HubStatus"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out

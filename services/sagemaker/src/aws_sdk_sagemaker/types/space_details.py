"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.non_empty_string64
    import aws_sdk_sagemaker.types.ownership_settings_summary
    import aws_sdk_sagemaker.types.space_name
    import aws_sdk_sagemaker.types.space_settings_summary
    import aws_sdk_sagemaker.types.space_sharing_settings_summary
    import aws_sdk_sagemaker.types.space_status


class SpaceDetails(TypedDict, closed=True):
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the associated domain.</p>"""
    space_name: NotRequired["aws_sdk_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.space_status.SpaceStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    space_settings_summary: NotRequired[
        "aws_sdk_sagemaker.types.space_settings_summary.SpaceSettingsSummary"
    ]
    """<p>Specifies summary information about the space settings.</p>"""
    space_sharing_settings_summary: NotRequired[
        "aws_sdk_sagemaker.types.space_sharing_settings_summary.SpaceSharingSettingsSummary"
    ]
    """<p>Specifies summary information about the space sharing settings.</p>"""
    ownership_settings_summary: NotRequired[
        "aws_sdk_sagemaker.types.ownership_settings_summary.OwnershipSettingsSummary"
    ]
    """<p>Specifies summary information about the ownership settings.</p>"""
    space_display_name: NotRequired[
        "aws_sdk_sagemaker.types.non_empty_string64.NonEmptyString64"
    ]
    """<p>The name of the space that appears in the Studio UI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceDetails) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "status" in value:
        import aws_sdk_sagemaker.types.space_status

        out["Status"] = aws_sdk_sagemaker.types.space_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "space_settings_summary" in value:
        import aws_sdk_sagemaker.types.space_settings_summary

        out["SpaceSettingsSummary"] = (
            aws_sdk_sagemaker.types.space_settings_summary.serialize_aws_json_1_1(
                value["space_settings_summary"]
            )
        )
    if "space_sharing_settings_summary" in value:
        import aws_sdk_sagemaker.types.space_sharing_settings_summary

        out["SpaceSharingSettingsSummary"] = (
            aws_sdk_sagemaker.types.space_sharing_settings_summary.serialize_aws_json_1_1(
                value["space_sharing_settings_summary"]
            )
        )
    if "ownership_settings_summary" in value:
        import aws_sdk_sagemaker.types.ownership_settings_summary

        out["OwnershipSettingsSummary"] = (
            aws_sdk_sagemaker.types.ownership_settings_summary.serialize_aws_json_1_1(
                value["ownership_settings_summary"]
            )
        )
    if "space_display_name" in value:
        out["SpaceDisplayName"] = value["space_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceDetails:
    out: SpaceDetails = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.space_status

        out["status"] = aws_sdk_sagemaker.types.space_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "SpaceSettingsSummary" in data:
        import aws_sdk_sagemaker.types.space_settings_summary

        out["space_settings_summary"] = (
            aws_sdk_sagemaker.types.space_settings_summary.deserialize_aws_json_1_1(
                data["SpaceSettingsSummary"]
            )
        )
    if "SpaceSharingSettingsSummary" in data:
        import aws_sdk_sagemaker.types.space_sharing_settings_summary

        out["space_sharing_settings_summary"] = (
            aws_sdk_sagemaker.types.space_sharing_settings_summary.deserialize_aws_json_1_1(
                data["SpaceSharingSettingsSummary"]
            )
        )
    if "OwnershipSettingsSummary" in data:
        import aws_sdk_sagemaker.types.ownership_settings_summary

        out["ownership_settings_summary"] = (
            aws_sdk_sagemaker.types.ownership_settings_summary.deserialize_aws_json_1_1(
                data["OwnershipSettingsSummary"]
            )
        )
    if "SpaceDisplayName" in data:
        out["space_display_name"] = data["SpaceDisplayName"]
    return out

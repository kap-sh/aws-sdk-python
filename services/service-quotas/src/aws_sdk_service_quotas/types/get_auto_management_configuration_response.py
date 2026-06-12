"""Generated from Smithy shape ``com.amazonaws.servicequotas#GetAutoManagementConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.amazon_resource_name
    import aws_sdk_service_quotas.types.exclusion_quota_list
    import aws_sdk_service_quotas.types.opt_in_level
    import aws_sdk_service_quotas.types.opt_in_status
    import aws_sdk_service_quotas.types.opt_in_type


class GetAutoManagementConfigurationResponse(TypedDict):
    opt_in_level: NotRequired["aws_sdk_service_quotas.types.opt_in_level.OptInLevel"]
    """<p>Information on the opt-in level for Automatic Management. Only Amazon Web Services account level is supported.</p>"""
    opt_in_type: NotRequired["aws_sdk_service_quotas.types.opt_in_type.OptInType"]
    """<p>Information on the opt-in type for Automatic Management. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.</p>"""
    notification_arn: NotRequired[
        "aws_sdk_service_quotas.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The <a href=\"https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table\">User Notifications</a> Amazon Resource Name (ARN) for Automatic Management notifications.</p>"""
    opt_in_status: NotRequired["aws_sdk_service_quotas.types.opt_in_status.OptInStatus"]
    """<p>Status on whether Automatic Management is started or stopped.</p>"""
    exclusion_list: NotRequired[
        "aws_sdk_service_quotas.types.exclusion_quota_list.ExclusionQuotaList"
    ]
    """<p>List of Amazon Web Services services excluded from Automatic Management. You won't be notified of Service Quotas utilization for Amazon Web Services services added to the Automatic Management exclusion list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAutoManagementConfigurationResponse) -> dict:
    out: dict = {}
    if "opt_in_level" in value:
        import aws_sdk_service_quotas.types.opt_in_level

        out["OptInLevel"] = (
            aws_sdk_service_quotas.types.opt_in_level.serialize_aws_json_1_1(
                value["opt_in_level"]
            )
        )
    if "opt_in_type" in value:
        import aws_sdk_service_quotas.types.opt_in_type

        out["OptInType"] = (
            aws_sdk_service_quotas.types.opt_in_type.serialize_aws_json_1_1(
                value["opt_in_type"]
            )
        )
    if "notification_arn" in value:
        out["NotificationArn"] = value["notification_arn"]
    if "opt_in_status" in value:
        import aws_sdk_service_quotas.types.opt_in_status

        out["OptInStatus"] = (
            aws_sdk_service_quotas.types.opt_in_status.serialize_aws_json_1_1(
                value["opt_in_status"]
            )
        )
    if "exclusion_list" in value:
        import aws_sdk_service_quotas.types.exclusion_quota_list

        out["ExclusionList"] = (
            aws_sdk_service_quotas.types.exclusion_quota_list.serialize_aws_json_1_1(
                value["exclusion_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAutoManagementConfigurationResponse:
    out: GetAutoManagementConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "OptInLevel" in data:
        import aws_sdk_service_quotas.types.opt_in_level

        out["opt_in_level"] = (
            aws_sdk_service_quotas.types.opt_in_level.deserialize_aws_json_1_1(
                data["OptInLevel"]
            )
        )
    if "OptInType" in data:
        import aws_sdk_service_quotas.types.opt_in_type

        out["opt_in_type"] = (
            aws_sdk_service_quotas.types.opt_in_type.deserialize_aws_json_1_1(
                data["OptInType"]
            )
        )
    if "NotificationArn" in data:
        out["notification_arn"] = data["NotificationArn"]
    if "OptInStatus" in data:
        import aws_sdk_service_quotas.types.opt_in_status

        out["opt_in_status"] = (
            aws_sdk_service_quotas.types.opt_in_status.deserialize_aws_json_1_1(
                data["OptInStatus"]
            )
        )
    if "ExclusionList" in data:
        import aws_sdk_service_quotas.types.exclusion_quota_list

        out["exclusion_list"] = (
            aws_sdk_service_quotas.types.exclusion_quota_list.deserialize_aws_json_1_1(
                data["ExclusionList"]
            )
        )
    return out

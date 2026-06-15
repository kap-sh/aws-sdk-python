"""Generated from Smithy shape ``com.amazonaws.servicequotas#UpdateAutoManagementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.amazon_resource_name
    import aws_sdk_service_quotas.types.exclusion_list
    import aws_sdk_service_quotas.types.opt_in_type


class UpdateAutoManagementRequest(TypedDict):
    opt_in_type: NotRequired["aws_sdk_service_quotas.types.opt_in_type.OptInType"]
    """<p>Information on the opt-in type for your Automatic Management configuration. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.</p>"""
    notification_arn: NotRequired[
        "aws_sdk_service_quotas.types.amazon_resource_name.AmazonResourceName"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table\">User Notifications</a> Amazon Resource Name (ARN) for Automatic Management notifications you want to update.</p>"""
    exclusion_list: NotRequired[
        "aws_sdk_service_quotas.types.exclusion_list.ExclusionList"
    ]
    """<p>List of Amazon Web Services services you want to exclude from Automatic Management. You won't be notified of Service Quotas utilization for Amazon Web Services services added to the Automatic Management exclusion list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAutoManagementRequest) -> dict:
    out: dict = {}
    if "opt_in_type" in value:
        import aws_sdk_service_quotas.types.opt_in_type

        out["OptInType"] = (
            aws_sdk_service_quotas.types.opt_in_type.serialize_aws_json_1_1(
                value["opt_in_type"]
            )
        )
    if "notification_arn" in value:
        out["NotificationArn"] = value["notification_arn"]
    if "exclusion_list" in value:
        import aws_sdk_service_quotas.types.exclusion_list

        out["ExclusionList"] = (
            aws_sdk_service_quotas.types.exclusion_list.serialize_aws_json_1_1(
                value["exclusion_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAutoManagementRequest:
    out: UpdateAutoManagementRequest = {}  # type: ignore[typeddict-item]
    if "OptInType" in data:
        import aws_sdk_service_quotas.types.opt_in_type

        out["opt_in_type"] = (
            aws_sdk_service_quotas.types.opt_in_type.deserialize_aws_json_1_1(
                data["OptInType"]
            )
        )
    if "NotificationArn" in data:
        out["notification_arn"] = data["NotificationArn"]
    if "ExclusionList" in data:
        import aws_sdk_service_quotas.types.exclusion_list

        out["exclusion_list"] = (
            aws_sdk_service_quotas.types.exclusion_list.deserialize_aws_json_1_1(
                data["ExclusionList"]
            )
        )
    return out

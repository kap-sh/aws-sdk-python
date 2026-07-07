"""Generated from Smithy shape ``com.amazonaws.servicequotas#StartAutoManagementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_quotas.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.amazon_resource_name
    import aws_sdk_service_quotas.types.exclusion_list
    import aws_sdk_service_quotas.types.opt_in_level
    import aws_sdk_service_quotas.types.opt_in_type


class StartAutoManagementRequest(TypedDict, closed=True):
    opt_in_level: "aws_sdk_service_quotas.types.opt_in_level.OptInLevel"
    """<p>Sets the opt-in level for Automatic Management. Only Amazon Web Services account level is supported.</p>"""
    opt_in_type: "aws_sdk_service_quotas.types.opt_in_type.OptInType"
    """<p>Sets the opt-in type for Automatic Management. There are two modes: Notify only and Notify and Auto-Adjust. Currently, only NotifyOnly is available.</p>"""
    notification_arn: NotRequired[
        "aws_sdk_service_quotas.types.amazon_resource_name.AmazonResourceName"
    ]
    r"""<p>The <a href=\"https://docs.aws.amazon.com/notifications/latest/userguide/resource-level-permissions.html#rlp-table\">User Notifications</a> Amazon Resource Name (ARN) for Automatic Management notifications.</p>"""
    exclusion_list: NotRequired[
        "aws_sdk_service_quotas.types.exclusion_list.ExclusionList"
    ]
    """<p>List of Amazon Web Services services excluded from Automatic Management. You won't be notified of Service Quotas utilization for Amazon Web Services services added to the Automatic Management exclusion list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartAutoManagementRequest) -> dict:
    out: dict = {}
    import aws_sdk_service_quotas.types.opt_in_level

    out["OptInLevel"] = (
        aws_sdk_service_quotas.types.opt_in_level.serialize_aws_json_1_1(
            value["opt_in_level"]
        )
    )
    import aws_sdk_service_quotas.types.opt_in_type

    out["OptInType"] = aws_sdk_service_quotas.types.opt_in_type.serialize_aws_json_1_1(
        value["opt_in_type"]
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


def deserialize_aws_json_1_1(data: dict) -> StartAutoManagementRequest:
    out: StartAutoManagementRequest = {}  # type: ignore[typeddict-item]
    if "OptInLevel" in data:
        import aws_sdk_service_quotas.types.opt_in_level

        out["opt_in_level"] = (
            aws_sdk_service_quotas.types.opt_in_level.deserialize_aws_json_1_1(
                data["OptInLevel"]
            )
        )
    else:
        raise DeserializationError("StartAutoManagementRequest.opt_in_level required")
    if "OptInType" in data:
        import aws_sdk_service_quotas.types.opt_in_type

        out["opt_in_type"] = (
            aws_sdk_service_quotas.types.opt_in_type.deserialize_aws_json_1_1(
                data["OptInType"]
            )
        )
    else:
        raise DeserializationError("StartAutoManagementRequest.opt_in_type required")
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

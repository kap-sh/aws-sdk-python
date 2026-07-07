"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.membership_job_log_status
    import aws_sdk_cleanrooms.types.membership_payment_configuration
    import aws_sdk_cleanrooms.types.membership_protected_job_result_configuration
    import aws_sdk_cleanrooms.types.membership_protected_query_result_configuration
    import aws_sdk_cleanrooms.types.membership_query_log_status
    import aws_sdk_cleanrooms.types.tag_map


class CreateMembershipInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique ID for the associated collaboration.</p>"""
    query_log_status: (
        "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
    )
    """<p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
    ]
    """<p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    tags: NotRequired["aws_sdk_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    default_result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
    ]
    """<p>The default protected query result configuration as specified by the member who can receive results.</p>"""
    default_job_result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
    ]
    """<p>The default job result configuration that determines how job results are protected and managed within this membership. This configuration applies to all jobs.</p>"""
    payment_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.membership_payment_configuration.MembershipPaymentConfiguration"
    ]
    """<p>The payment responsibilities accepted by the collaboration member.</p> <p>Not required if the collaboration member has the member ability to run queries. </p> <p>Required if the collaboration member doesn't have the member ability to run queries but is configured as a payer by the collaboration creator. </p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether Amazon CloudWatch metrics have been enabled or disabled for the membership.</p> <p>Amazon CloudWatch metrics are only available when the collaboration has metrics enabled. This option can be set by collaboration members who have the ability to run queries (analysis runners) or by members who are configured as payers.</p> <p>When <code>true</code>, metrics about query execution are collected in Amazon CloudWatch. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMembershipInput) -> dict:
    out: dict = {}
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    import aws_sdk_cleanrooms.types.membership_query_log_status

    out["queryLogStatus"] = (
        aws_sdk_cleanrooms.types.membership_query_log_status.serialize_json(
            value["query_log_status"]
        )
    )
    if "job_log_status" in value:
        import aws_sdk_cleanrooms.types.membership_job_log_status

        out["jobLogStatus"] = (
            aws_sdk_cleanrooms.types.membership_job_log_status.serialize_json(
                value["job_log_status"]
            )
        )
    if "tags" in value:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "default_result_configuration" in value:
        import aws_sdk_cleanrooms.types.membership_protected_query_result_configuration

        out["defaultResultConfiguration"] = (
            aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.serialize_json(
                value["default_result_configuration"]
            )
        )
    if "default_job_result_configuration" in value:
        import aws_sdk_cleanrooms.types.membership_protected_job_result_configuration

        out["defaultJobResultConfiguration"] = (
            aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.serialize_json(
                value["default_job_result_configuration"]
            )
        )
    if "payment_configuration" in value:
        import aws_sdk_cleanrooms.types.membership_payment_configuration

        out["paymentConfiguration"] = (
            aws_sdk_cleanrooms.types.membership_payment_configuration.serialize_json(
                value["payment_configuration"]
            )
        )
    if "is_metrics_enabled" in value:
        out["isMetricsEnabled"] = value["is_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> CreateMembershipInput:
    out: CreateMembershipInput = {}  # type: ignore[typeddict-item]
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "CreateMembershipInput.collaboration_identifier required"
        )
    if "queryLogStatus" in data:
        import aws_sdk_cleanrooms.types.membership_query_log_status

        out["query_log_status"] = (
            aws_sdk_cleanrooms.types.membership_query_log_status.deserialize_json(
                data["queryLogStatus"]
            )
        )
    else:
        raise DeserializationError("CreateMembershipInput.query_log_status required")
    if "jobLogStatus" in data:
        import aws_sdk_cleanrooms.types.membership_job_log_status

        out["job_log_status"] = (
            aws_sdk_cleanrooms.types.membership_job_log_status.deserialize_json(
                data["jobLogStatus"]
            )
        )
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if "defaultResultConfiguration" in data:
        import aws_sdk_cleanrooms.types.membership_protected_query_result_configuration

        out["default_result_configuration"] = (
            aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.deserialize_json(
                data["defaultResultConfiguration"]
            )
        )
    if "defaultJobResultConfiguration" in data:
        import aws_sdk_cleanrooms.types.membership_protected_job_result_configuration

        out["default_job_result_configuration"] = (
            aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.deserialize_json(
                data["defaultJobResultConfiguration"]
            )
        )
    if "paymentConfiguration" in data:
        import aws_sdk_cleanrooms.types.membership_payment_configuration

        out["payment_configuration"] = (
            aws_sdk_cleanrooms.types.membership_payment_configuration.deserialize_json(
                data["paymentConfiguration"]
            )
        )
    if "isMetricsEnabled" in data:
        out["is_metrics_enabled"] = data["isMetricsEnabled"]
    return out

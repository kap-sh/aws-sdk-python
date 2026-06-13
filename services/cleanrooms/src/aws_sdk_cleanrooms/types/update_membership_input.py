"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateMembershipInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.membership_job_log_status
    import aws_sdk_cleanrooms.types.membership_protected_job_result_configuration
    import aws_sdk_cleanrooms.types.membership_protected_query_result_configuration
    import aws_sdk_cleanrooms.types.membership_query_log_status
    import aws_sdk_cleanrooms.types.update_membership_payment_configuration


class UpdateMembershipInput(TypedDict):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership.</p>"""
    query_log_status: NotRequired[
        "aws_sdk_cleanrooms.types.membership_query_log_status.MembershipQueryLogStatus"
    ]
    """<p>An indicator as to whether query logging has been enabled or disabled for the membership.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "aws_sdk_cleanrooms.types.membership_job_log_status.MembershipJobLogStatus"
    ]
    """<p>An indicator as to whether job logging has been enabled or disabled for the collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    default_result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.membership_protected_query_result_configuration.MembershipProtectedQueryResultConfiguration"
    ]
    """<p>The default protected query result configuration as specified by the member who can receive results.</p>"""
    default_job_result_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.membership_protected_job_result_configuration.MembershipProtectedJobResultConfiguration"
    ]
    """<p> The default job result configuration.</p>"""
    membership_payment_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.update_membership_payment_configuration.UpdateMembershipPaymentConfiguration"
    ]
    """<p>The payment configuration to update for the membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMembershipInput) -> dict:
    out: dict = {}
    if "query_log_status" in value:
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
    if "membership_payment_configuration" in value:
        import aws_sdk_cleanrooms.types.update_membership_payment_configuration

        out["membershipPaymentConfiguration"] = (
            aws_sdk_cleanrooms.types.update_membership_payment_configuration.serialize_json(
                value["membership_payment_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMembershipInput:
    out: UpdateMembershipInput = {}  # type: ignore[typeddict-item]
    if "queryLogStatus" in data:
        import aws_sdk_cleanrooms.types.membership_query_log_status

        out["query_log_status"] = (
            aws_sdk_cleanrooms.types.membership_query_log_status.deserialize_json(
                data["queryLogStatus"]
            )
        )
    if "jobLogStatus" in data:
        import aws_sdk_cleanrooms.types.membership_job_log_status

        out["job_log_status"] = (
            aws_sdk_cleanrooms.types.membership_job_log_status.deserialize_json(
                data["jobLogStatus"]
            )
        )
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
    if "membershipPaymentConfiguration" in data:
        import aws_sdk_cleanrooms.types.update_membership_payment_configuration

        out["membership_payment_configuration"] = (
            aws_sdk_cleanrooms.types.update_membership_payment_configuration.deserialize_json(
                data["membershipPaymentConfiguration"]
            )
        )
    return out

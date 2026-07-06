"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerLogsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsAmazonMqBrokerLogsDetails(TypedDict, closed=True):
    audit: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Activates audit logging. Every user management action made using JMX or the ActiveMQ Web Console is logged. Doesn't apply to RabbitMQ brokers. </p>"""
    general: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Activates general logging. </p>"""
    audit_log_group: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The location of the CloudWatch Logs log group where audit logs are sent. </p>"""
    general_log_group: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The location of the CloudWatch Logs log group where general logs are sent. </p>"""
    pending: NotRequired[
        "aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details.AwsAmazonMqBrokerLogsPendingDetails"
    ]
    """<p> The list of information about logs that are to be turned on for the specified broker. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerLogsDetails) -> dict:
    out: dict = {}
    if "audit" in value:
        out["Audit"] = value["audit"]
    if "general" in value:
        out["General"] = value["general"]
    if "audit_log_group" in value:
        out["AuditLogGroup"] = value["audit_log_group"]
    if "general_log_group" in value:
        out["GeneralLogGroup"] = value["general_log_group"]
    if "pending" in value:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details

        out["Pending"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details.serialize_json(
                value["pending"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerLogsDetails:
    out: AwsAmazonMqBrokerLogsDetails = {}  # type: ignore[typeddict-item]
    if "Audit" in data:
        out["audit"] = data["Audit"]
    if "General" in data:
        out["general"] = data["General"]
    if "AuditLogGroup" in data:
        out["audit_log_group"] = data["AuditLogGroup"]
    if "GeneralLogGroup" in data:
        out["general_log_group"] = data["GeneralLogGroup"]
    if "Pending" in data:
        import aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details

        out["pending"] = (
            aws_sdk_securityhub.types.aws_amazon_mq_broker_logs_pending_details.deserialize_json(
                data["Pending"]
            )
        )
    return out

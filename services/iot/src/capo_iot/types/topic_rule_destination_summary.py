"""Generated from Smithy shape ``com.amazonaws.iot#TopicRuleDestinationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.created_at_date
    import capo_iot.types.http_url_destination_summary
    import capo_iot.types.last_updated_at_date
    import capo_iot.types.string
    import capo_iot.types.topic_rule_destination_status
    import capo_iot.types.vpc_destination_summary


class TopicRuleDestinationSummary(TypedDict, closed=True):
    arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>The topic rule destination ARN.</p>"""
    status: NotRequired[
        "capo_iot.types.topic_rule_destination_status.TopicRuleDestinationStatus"
    ]
    """<p>The status of the topic rule destination. Valid values are:</p> <dl> <dt>IN_PROGRESS</dt> <dd> <p>A topic rule destination was created but has not been confirmed. You can set <code>status</code> to <code>IN_PROGRESS</code> by calling <code>UpdateTopicRuleDestination</code>. Calling <code>UpdateTopicRuleDestination</code> causes a new confirmation challenge to be sent to your confirmation endpoint.</p> </dd> <dt>ENABLED</dt> <dd> <p>Confirmation was completed, and traffic to this destination is allowed. You can set <code>status</code> to <code>DISABLED</code> by calling <code>UpdateTopicRuleDestination</code>.</p> </dd> <dt>DISABLED</dt> <dd> <p>Confirmation was completed, and traffic to this destination is not allowed. You can set <code>status</code> to <code>ENABLED</code> by calling <code>UpdateTopicRuleDestination</code>.</p> </dd> <dt>ERROR</dt> <dd> <p>Confirmation could not be completed, for example if the confirmation timed out. You can call <code>GetTopicRuleDestination</code> for details about the error. You can set <code>status</code> to <code>IN_PROGRESS</code> by calling <code>UpdateTopicRuleDestination</code>. Calling <code>UpdateTopicRuleDestination</code> causes a new confirmation challenge to be sent to your confirmation endpoint.</p> </dd> </dl>"""
    created_at: NotRequired["capo_iot.types.created_at_date.CreatedAtDate"]
    """<p>The date and time when the topic rule destination was created.</p>"""
    last_updated_at: NotRequired[
        "capo_iot.types.last_updated_at_date.LastUpdatedAtDate"
    ]
    """<p>The date and time when the topic rule destination was last updated.</p>"""
    status_reason: NotRequired["capo_iot.types.string.String"]
    """<p>The reason the topic rule destination is in the current status.</p>"""
    http_url_summary: NotRequired[
        "capo_iot.types.http_url_destination_summary.HttpUrlDestinationSummary"
    ]
    """<p>Information about the HTTP URL.</p>"""
    vpc_destination_summary: NotRequired[
        "capo_iot.types.vpc_destination_summary.VpcDestinationSummary"
    ]
    """<p>Information about the virtual private cloud (VPC) connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicRuleDestinationSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import capo_iot.types.topic_rule_destination_status

        out["status"] = capo_iot.types.topic_rule_destination_status.serialize_json(
            value["status"]
        )
    if "created_at" in value:
        import capo_iot.types.created_at_date

        out["createdAt"] = capo_iot.types.created_at_date.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_iot.types.last_updated_at_date

        out["lastUpdatedAt"] = capo_iot.types.last_updated_at_date.serialize_json(
            value["last_updated_at"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "http_url_summary" in value:
        import capo_iot.types.http_url_destination_summary

        out["httpUrlSummary"] = (
            capo_iot.types.http_url_destination_summary.serialize_json(
                value["http_url_summary"]
            )
        )
    if "vpc_destination_summary" in value:
        import capo_iot.types.vpc_destination_summary

        out["vpcDestinationSummary"] = (
            capo_iot.types.vpc_destination_summary.serialize_json(
                value["vpc_destination_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> TopicRuleDestinationSummary:
    out: TopicRuleDestinationSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import capo_iot.types.topic_rule_destination_status

        out["status"] = capo_iot.types.topic_rule_destination_status.deserialize_json(
            data["status"]
        )
    if "createdAt" in data:
        import capo_iot.types.created_at_date

        out["created_at"] = capo_iot.types.created_at_date.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_iot.types.last_updated_at_date

        out["last_updated_at"] = capo_iot.types.last_updated_at_date.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "httpUrlSummary" in data:
        import capo_iot.types.http_url_destination_summary

        out["http_url_summary"] = (
            capo_iot.types.http_url_destination_summary.deserialize_json(
                data["httpUrlSummary"]
            )
        )
    if "vpcDestinationSummary" in data:
        import capo_iot.types.vpc_destination_summary

        out["vpc_destination_summary"] = (
            capo_iot.types.vpc_destination_summary.deserialize_json(
                data["vpcDestinationSummary"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#RuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_message
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.readiness
    import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp


class RuleResult(TypedDict):
    last_checked_timestamp: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.ReadinessCheckTimestamp"
    ]
    """<p>The time the resource was last checked for readiness, in ISO-8601 format, UTC.</p>"""
    messages: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_message.__listOfMessage"
    ]
    """<p>Details about the resource's readiness.</p>"""
    readiness: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness.Readiness"
    ]
    """<p>The readiness at rule level.</p>"""
    rule_id: NotRequired["aws_sdk_route53_recovery_readiness.types.__string.__string"]
    """<p>The identifier of the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleResult) -> dict:
    out: dict = {}
    if "last_checked_timestamp" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp

        out["lastCheckedTimestamp"] = (
            aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.serialize_json(
                value["last_checked_timestamp"]
            )
        )
    if "messages" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_message

        out["messages"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_message.serialize_json(
                value["messages"]
            )
        )
    if "readiness" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    return out


def deserialize_json(data: dict) -> RuleResult:
    out: RuleResult = {}  # type: ignore[typeddict-item]
    if "lastCheckedTimestamp" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp

        out["last_checked_timestamp"] = (
            aws_sdk_route53_recovery_readiness.types.readiness_check_timestamp.deserialize_json(
                data["lastCheckedTimestamp"]
            )
        )
    if "messages" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_message

        out["messages"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_message.deserialize_json(
                data["messages"]
            )
        )
    if "readiness" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "ruleId" in data:
        out["rule_id"] = data["ruleId"]
    return out

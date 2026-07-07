"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetReadinessCheckResourceStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_rule_result
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.readiness


class GetReadinessCheckResourceStatusResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness.Readiness"
    ]
    """<p>The readiness at a rule level.</p>"""
    rules: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_rule_result.__listOfRuleResult"
    ]
    """<p>Details of the rule's results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetReadinessCheckResourceStatusResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "readiness" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "rules" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_rule_result

        out["rules"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_rule_result.serialize_json(
                value["rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetReadinessCheckResourceStatusResponse:
    out: GetReadinessCheckResourceStatusResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "readiness" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "rules" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_rule_result

        out["rules"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_rule_result.deserialize_json(
                data["rules"]
            )
        )
    return out

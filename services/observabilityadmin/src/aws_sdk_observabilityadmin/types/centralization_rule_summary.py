"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationRuleSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_failure_reason
    import aws_sdk_observabilityadmin.types.region
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.rule_health
    import aws_sdk_observabilityadmin.types.rule_name


class CentralizationRuleSummary(TypedDict):
    rule_name: NotRequired["aws_sdk_observabilityadmin.types.rule_name.RuleName"]
    """<p>The name of the organization centralization rule.</p>"""
    rule_arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the organization centralization rule.</p>"""
    creator_account_id: NotRequired["str"]
    """<p>The Amazon Web Services Account that created the organization centralization rule.</p>"""
    created_time_stamp: NotRequired["int"]
    """<p>The timestamp when the organization centralization rule was created.</p>"""
    created_region: NotRequired["aws_sdk_observabilityadmin.types.region.Region"]
    """<p>The Amazon Web Services region where the organization centralization rule was created.</p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p>The timestamp when the organization centralization rule was last updated.</p>"""
    rule_health: NotRequired["aws_sdk_observabilityadmin.types.rule_health.RuleHealth"]
    """<p>The health status of the organization centralization rule.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_observabilityadmin.types.centralization_failure_reason.CentralizationFailureReason"
    ]
    """<p>The reason why an organization centralization rule is marked UNHEALTHY.</p>"""
    destination_account_id: NotRequired["str"]
    """<p>The primary destination account of the organization centralization rule.</p>"""
    destination_region: NotRequired["aws_sdk_observabilityadmin.types.region.Region"]
    """<p>The primary destination region of the organization centralization rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationRuleSummary) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "creator_account_id" in value:
        out["CreatorAccountId"] = value["creator_account_id"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "created_region" in value:
        out["CreatedRegion"] = value["created_region"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "rule_health" in value:
        import aws_sdk_observabilityadmin.types.rule_health

        out["RuleHealth"] = aws_sdk_observabilityadmin.types.rule_health.serialize_json(
            value["rule_health"]
        )
    if "failure_reason" in value:
        import aws_sdk_observabilityadmin.types.centralization_failure_reason

        out["FailureReason"] = (
            aws_sdk_observabilityadmin.types.centralization_failure_reason.serialize_json(
                value["failure_reason"]
            )
        )
    if "destination_account_id" in value:
        out["DestinationAccountId"] = value["destination_account_id"]
    if "destination_region" in value:
        out["DestinationRegion"] = value["destination_region"]
    return out


def deserialize_json(data: dict) -> CentralizationRuleSummary:
    out: CentralizationRuleSummary = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "CreatorAccountId" in data:
        out["creator_account_id"] = data["CreatorAccountId"]
    if "CreatedTimeStamp" in data:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if "CreatedRegion" in data:
        out["created_region"] = data["CreatedRegion"]
    if "LastUpdateTimeStamp" in data:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if "RuleHealth" in data:
        import aws_sdk_observabilityadmin.types.rule_health

        out["rule_health"] = (
            aws_sdk_observabilityadmin.types.rule_health.deserialize_json(
                data["RuleHealth"]
            )
        )
    if "FailureReason" in data:
        import aws_sdk_observabilityadmin.types.centralization_failure_reason

        out["failure_reason"] = (
            aws_sdk_observabilityadmin.types.centralization_failure_reason.deserialize_json(
                data["FailureReason"]
            )
        )
    if "DestinationAccountId" in data:
        out["destination_account_id"] = data["DestinationAccountId"]
    if "DestinationRegion" in data:
        out["destination_region"] = data["DestinationRegion"]
    return out

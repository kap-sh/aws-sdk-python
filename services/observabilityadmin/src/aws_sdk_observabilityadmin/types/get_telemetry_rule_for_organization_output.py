"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryRuleForOrganizationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.is_replicated
    import aws_sdk_observabilityadmin.types.region
    import aws_sdk_observabilityadmin.types.region_statuses
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.rule_name
    import aws_sdk_observabilityadmin.types.telemetry_rule


class GetTelemetryRuleForOrganizationOutput(TypedDict):
    rule_name: NotRequired["aws_sdk_observabilityadmin.types.rule_name.RuleName"]
    """<p> The name of the organization telemetry rule. </p>"""
    rule_arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the organization telemetry rule. </p>"""
    created_time_stamp: NotRequired["int"]
    """<p> The timestamp when the organization telemetry rule was created. </p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p> The timestamp when the organization telemetry rule was last updated. </p>"""
    telemetry_rule: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_rule.TelemetryRule"
    ]
    """<p> The configuration details of the organization telemetry rule. </p>"""
    home_region: NotRequired["aws_sdk_observabilityadmin.types.region.Region"]
    """<p> The Amazon Web Services Region where the organization telemetry rule was originally created. For replicated rules in spoke regions, this indicates the region that manages the rule. For rules created without multi-region scope, this field is not present. </p>"""
    is_replicated: NotRequired[
        "aws_sdk_observabilityadmin.types.is_replicated.IsReplicated"
    ]
    """<p> Indicates whether this organization telemetry rule is a replica that was created in this region through multi-region fan-out from the home region. Replicated rules cannot be directly updated or deleted in the spoke region. To modify a replicated rule, make changes in the home region. </p>"""
    region_statuses: NotRequired[
        "aws_sdk_observabilityadmin.types.region_statuses.RegionStatuses"
    ]
    """<p> A list of per-region replication statuses for the organization telemetry rule. Each entry indicates the replication status of the rule in a specific spoke region. This field is only present for rules created with multi-region scope. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryRuleForOrganizationOutput) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "rule_arn" in value:
        out["RuleArn"] = value["rule_arn"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "telemetry_rule" in value:
        import aws_sdk_observabilityadmin.types.telemetry_rule

        out["TelemetryRule"] = (
            aws_sdk_observabilityadmin.types.telemetry_rule.serialize_json(
                value["telemetry_rule"]
            )
        )
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    if "is_replicated" in value:
        out["IsReplicated"] = value["is_replicated"]
    if "region_statuses" in value:
        import aws_sdk_observabilityadmin.types.region_statuses

        out["RegionStatuses"] = (
            aws_sdk_observabilityadmin.types.region_statuses.serialize_json(
                value["region_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTelemetryRuleForOrganizationOutput:
    out: GetTelemetryRuleForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "RuleArn" in data:
        out["rule_arn"] = data["RuleArn"]
    if "CreatedTimeStamp" in data:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if "LastUpdateTimeStamp" in data:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if "TelemetryRule" in data:
        import aws_sdk_observabilityadmin.types.telemetry_rule

        out["telemetry_rule"] = (
            aws_sdk_observabilityadmin.types.telemetry_rule.deserialize_json(
                data["TelemetryRule"]
            )
        )
    if "HomeRegion" in data:
        out["home_region"] = data["HomeRegion"]
    if "IsReplicated" in data:
        out["is_replicated"] = data["IsReplicated"]
    if "RegionStatuses" in data:
        import aws_sdk_observabilityadmin.types.region_statuses

        out["region_statuses"] = (
            aws_sdk_observabilityadmin.types.region_statuses.deserialize_json(
                data["RegionStatuses"]
            )
        )
    return out

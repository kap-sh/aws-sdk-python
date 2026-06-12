"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTelemetryRulesForOrganizationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.account_identifiers
    import aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_max_results
    import aws_sdk_observabilityadmin.types.next_token
    import aws_sdk_observabilityadmin.types.organization_unit_identifiers


class ListTelemetryRulesForOrganizationInput(TypedDict):
    rule_name_prefix: NotRequired["str"]
    """<p> A string to filter organization telemetry rules whose names begin with the specified prefix. </p>"""
    source_account_ids: NotRequired[
        "aws_sdk_observabilityadmin.types.account_identifiers.AccountIdentifiers"
    ]
    """<p> The list of account IDs to filter organization telemetry rules by their source accounts. </p>"""
    source_organization_unit_ids: NotRequired[
        "aws_sdk_observabilityadmin.types.organization_unit_identifiers.OrganizationUnitIdentifiers"
    ]
    """<p> The list of organizational unit IDs to filter organization telemetry rules by their source organizational units. </p>"""
    max_results: NotRequired[
        "aws_sdk_observabilityadmin.types.list_telemetry_rules_for_organization_max_results.ListTelemetryRulesForOrganizationMaxResults"
    ]
    """<p> The maximum number of organization telemetry rules to return in a single call. </p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p> The token for the next set of results. A previous call generates this token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTelemetryRulesForOrganizationInput) -> dict:
    out: dict = {}
    if "rule_name_prefix" in value:
        out["RuleNamePrefix"] = value["rule_name_prefix"]
    if "source_account_ids" in value:
        import aws_sdk_observabilityadmin.types.account_identifiers

        out["SourceAccountIds"] = (
            aws_sdk_observabilityadmin.types.account_identifiers.serialize_json(
                value["source_account_ids"]
            )
        )
    if "source_organization_unit_ids" in value:
        import aws_sdk_observabilityadmin.types.organization_unit_identifiers

        out["SourceOrganizationUnitIds"] = (
            aws_sdk_observabilityadmin.types.organization_unit_identifiers.serialize_json(
                value["source_organization_unit_ids"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTelemetryRulesForOrganizationInput:
    out: ListTelemetryRulesForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleNamePrefix" in data:
        out["rule_name_prefix"] = data["RuleNamePrefix"]
    if "SourceAccountIds" in data:
        import aws_sdk_observabilityadmin.types.account_identifiers

        out["source_account_ids"] = (
            aws_sdk_observabilityadmin.types.account_identifiers.deserialize_json(
                data["SourceAccountIds"]
            )
        )
    if "SourceOrganizationUnitIds" in data:
        import aws_sdk_observabilityadmin.types.organization_unit_identifiers

        out["source_organization_unit_ids"] = (
            aws_sdk_observabilityadmin.types.organization_unit_identifiers.deserialize_json(
                data["SourceOrganizationUnitIds"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out

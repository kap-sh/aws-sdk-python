"""Generated from Smithy shape ``com.amazonaws.ssm#TargetLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.accounts
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.boolean
    import capo_ssm.types.exclude_accounts
    import capo_ssm.types.execution_role_name
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.regions
    import capo_ssm.types.targets


class TargetLocation(TypedDict, closed=True):
    accounts: NotRequired["capo_ssm.types.accounts.Accounts"]
    """<p>The Amazon Web Services accounts targeted by the current Automation execution.</p>"""
    regions: NotRequired["capo_ssm.types.regions.Regions"]
    """<p>The Amazon Web Services Regions targeted by the current Automation execution.</p>"""
    target_location_max_concurrency: NotRequired[
        "capo_ssm.types.max_concurrency.MaxConcurrency"
    ]
    """<p>The maximum number of Amazon Web Services Regions and Amazon Web Services accounts allowed to run the Automation concurrently. <code>TargetLocationMaxConcurrency</code> has a default value of 1.</p>"""
    target_location_max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors allowed before the system stops queueing additional Automation executions for the currently running Automation. <code>TargetLocationMaxErrors</code> has a default value of 0.</p>"""
    execution_role_name: NotRequired[
        "capo_ssm.types.execution_role_name.ExecutionRoleName"
    ]
    """<p>The Automation execution role used by the currently running Automation. If not specified, the default value is <code>AWS-SystemsManager-AutomationExecutionRole</code>.</p>"""
    target_location_alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    include_child_organization_units: "capo_ssm.types.boolean.Boolean"
    """<p>Indicates whether to include child organizational units (OUs) that are children of the targeted OUs. The default is <code>false</code>.</p> <note> <p>This parameter is not supported by State Manager.</p> </note>"""
    exclude_accounts: NotRequired["capo_ssm.types.exclude_accounts.ExcludeAccounts"]
    """<p>Amazon Web Services accounts or organizational units to exclude as expanded targets.</p>"""
    targets: NotRequired["capo_ssm.types.targets.Targets"]
    """<p>A list of key-value mappings to target resources. If you specify values for this data type, you must also specify a value for <code>TargetParameterName</code>.</p> <p>This <code>Targets</code> parameter takes precedence over the <code>StartAutomationExecution:Targets</code> parameter if both are supplied.</p>"""
    targets_max_concurrency: NotRequired[
        "capo_ssm.types.max_concurrency.MaxConcurrency"
    ]
    """<p>The maximum number of targets allowed to run this task in parallel. This <code>TargetsMaxConcurrency</code> takes precedence over the <code>StartAutomationExecution:MaxConcurrency</code> parameter if both are supplied.</p>"""
    targets_max_errors: NotRequired["capo_ssm.types.max_errors.MaxErrors"]
    """<p>The maximum number of errors that are allowed before the system stops running the automation on additional targets. This <code>TargetsMaxErrors</code> parameter takes precedence over the <code>StartAutomationExecution:MaxErrors</code> parameter if both are supplied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetLocation) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_ssm.types.accounts

        out["Accounts"] = capo_ssm.types.accounts.serialize_aws_json_1_1(
            value["accounts"]
        )
    if "regions" in value:
        import capo_ssm.types.regions

        out["Regions"] = capo_ssm.types.regions.serialize_aws_json_1_1(value["regions"])
    if "target_location_max_concurrency" in value:
        out["TargetLocationMaxConcurrency"] = value["target_location_max_concurrency"]
    if "target_location_max_errors" in value:
        out["TargetLocationMaxErrors"] = value["target_location_max_errors"]
    if "execution_role_name" in value:
        out["ExecutionRoleName"] = value["execution_role_name"]
    if "target_location_alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["TargetLocationAlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["target_location_alarm_configuration"]
            )
        )
    out["IncludeChildOrganizationUnits"] = value.get(
        "include_child_organization_units", False
    )
    if "exclude_accounts" in value:
        import capo_ssm.types.exclude_accounts

        out["ExcludeAccounts"] = capo_ssm.types.exclude_accounts.serialize_aws_json_1_1(
            value["exclude_accounts"]
        )
    if "targets" in value:
        import capo_ssm.types.targets

        out["Targets"] = capo_ssm.types.targets.serialize_aws_json_1_1(value["targets"])
    if "targets_max_concurrency" in value:
        out["TargetsMaxConcurrency"] = value["targets_max_concurrency"]
    if "targets_max_errors" in value:
        out["TargetsMaxErrors"] = value["targets_max_errors"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetLocation:
    out: TargetLocation = {}  # type: ignore[typeddict-item]
    if data.get("Accounts") is not None:
        import capo_ssm.types.accounts

        out["accounts"] = capo_ssm.types.accounts.deserialize_aws_json_1_1(
            data["Accounts"]
        )
    if data.get("Regions") is not None:
        import capo_ssm.types.regions

        out["regions"] = capo_ssm.types.regions.deserialize_aws_json_1_1(
            data["Regions"]
        )
    if data.get("TargetLocationMaxConcurrency") is not None:
        out["target_location_max_concurrency"] = data["TargetLocationMaxConcurrency"]
    if data.get("TargetLocationMaxErrors") is not None:
        out["target_location_max_errors"] = data["TargetLocationMaxErrors"]
    if data.get("ExecutionRoleName") is not None:
        out["execution_role_name"] = data["ExecutionRoleName"]
    if data.get("TargetLocationAlarmConfiguration") is not None:
        import capo_ssm.types.alarm_configuration

        out["target_location_alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["TargetLocationAlarmConfiguration"]
            )
        )
    if data.get("IncludeChildOrganizationUnits") is not None:
        out["include_child_organization_units"] = data["IncludeChildOrganizationUnits"]
    else:
        out["include_child_organization_units"] = False
    if data.get("ExcludeAccounts") is not None:
        import capo_ssm.types.exclude_accounts

        out["exclude_accounts"] = (
            capo_ssm.types.exclude_accounts.deserialize_aws_json_1_1(
                data["ExcludeAccounts"]
            )
        )
    if data.get("Targets") is not None:
        import capo_ssm.types.targets

        out["targets"] = capo_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if data.get("TargetsMaxConcurrency") is not None:
        out["targets_max_concurrency"] = data["TargetsMaxConcurrency"]
    if data.get("TargetsMaxErrors") is not None:
        out["targets_max_errors"] = data["TargetsMaxErrors"]
    return out

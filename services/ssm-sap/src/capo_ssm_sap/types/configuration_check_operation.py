"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.configuration_check_type
    import capo_ssm_sap.types.operation_id
    import capo_ssm_sap.types.operation_status
    import capo_ssm_sap.types.rule_status_counts


class ConfigurationCheckOperation(TypedDict, closed=True):
    id: NotRequired["capo_ssm_sap.types.operation_id.OperationId"]
    """<p>The unique identifier of the configuration check operation.</p>"""
    application_id: NotRequired["capo_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application against which the configuration check was performed.</p>"""
    status: NotRequired["capo_ssm_sap.types.operation_status.OperationStatus"]
    """<p>The current status of the configuration check operation.</p>"""
    status_message: NotRequired["str"]
    """<p>A message providing additional details about the status of the configuration check operation.</p>"""
    configuration_check_id: NotRequired[
        "capo_ssm_sap.types.configuration_check_type.ConfigurationCheckType"
    ]
    """<p>The unique identifier of the configuration check that was performed.</p>"""
    configuration_check_name: NotRequired["str"]
    """<p>The name of the configuration check that was performed.</p>"""
    configuration_check_description: NotRequired["str"]
    """<p>A description of the configuration check that was performed.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>The time at which the configuration check operation started.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The time at which the configuration check operation completed.</p>"""
    rule_status_counts: NotRequired[
        "capo_ssm_sap.types.rule_status_counts.RuleStatusCounts"
    ]
    """<p>A summary of all the rule results, showing counts for each status type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckOperation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "status" in value:
        import capo_ssm_sap.types.operation_status

        out["Status"] = capo_ssm_sap.types.operation_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "configuration_check_id" in value:
        import capo_ssm_sap.types.configuration_check_type

        out["ConfigurationCheckId"] = (
            capo_ssm_sap.types.configuration_check_type.serialize_json(
                value["configuration_check_id"]
            )
        )
    if "configuration_check_name" in value:
        out["ConfigurationCheckName"] = value["configuration_check_name"]
    if "configuration_check_description" in value:
        out["ConfigurationCheckDescription"] = value["configuration_check_description"]
    if "start_time" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["StartTime"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["EndTime"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "rule_status_counts" in value:
        import capo_ssm_sap.types.rule_status_counts

        out["RuleStatusCounts"] = capo_ssm_sap.types.rule_status_counts.serialize_json(
            value["rule_status_counts"]
        )
    return out


def deserialize_json(data: dict) -> ConfigurationCheckOperation:
    out: ConfigurationCheckOperation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Status" in data:
        import capo_ssm_sap.types.operation_status

        out["status"] = capo_ssm_sap.types.operation_status.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ConfigurationCheckId" in data:
        import capo_ssm_sap.types.configuration_check_type

        out["configuration_check_id"] = (
            capo_ssm_sap.types.configuration_check_type.deserialize_json(
                data["ConfigurationCheckId"]
            )
        )
    if "ConfigurationCheckName" in data:
        out["configuration_check_name"] = data["ConfigurationCheckName"]
    if "ConfigurationCheckDescription" in data:
        out["configuration_check_description"] = data["ConfigurationCheckDescription"]
    if "StartTime" in data:
        import capo_ssm_sap.types._prelude.timestamp

        out["start_time"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_ssm_sap.types._prelude.timestamp

        out["end_time"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["EndTime"]
        )
    if "RuleStatusCounts" in data:
        import capo_ssm_sap.types.rule_status_counts

        out["rule_status_counts"] = (
            capo_ssm_sap.types.rule_status_counts.deserialize_json(
                data["RuleStatusCounts"]
            )
        )
    return out

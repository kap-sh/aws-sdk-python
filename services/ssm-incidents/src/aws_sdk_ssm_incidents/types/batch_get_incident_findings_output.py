"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ssm_incidents.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list
    import aws_sdk_ssm_incidents.types.finding_list

class BatchGetIncidentFindingsOutput(TypedDict):
    findings: "aws_sdk_ssm_incidents.types.finding_list.FindingList"
    """<p>Information about the requested findings.</p>"""
    errors: "aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list.BatchGetIncidentFindingsErrorList"
    """<p>A list of errors encountered during the operation.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.finding_list
    out["findings"] = aws_sdk_ssm_incidents.types.finding_list.serialize_json(value["findings"])
    import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list
    out["errors"] = aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetIncidentFindingsOutput:
    out: BatchGetIncidentFindingsOutput = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_ssm_incidents.types.finding_list
        out["findings"] = aws_sdk_ssm_incidents.types.finding_list.deserialize_json(data["findings"])
    else:
        raise DeserializationError("BatchGetIncidentFindingsOutput.findings required")
    if "errors" in data:
        import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list
        out["errors"] = aws_sdk_ssm_incidents.types.batch_get_incident_findings_error_list.deserialize_json(data["errors"])
    else:
        raise DeserializationError("BatchGetIncidentFindingsOutput.errors required")
    return out
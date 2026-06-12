"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ssm_incidents.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.finding_id_list

class BatchGetIncidentFindingsInput(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident for which you want to view finding details.</p>"""
    finding_ids: "aws_sdk_ssm_incidents.types.finding_id_list.FindingIdList"
    """<p>A list of IDs of findings for which you want to view details.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    import aws_sdk_ssm_incidents.types.finding_id_list
    out["findingIds"] = aws_sdk_ssm_incidents.types.finding_id_list.serialize_json(value["finding_ids"])
    return out


def deserialize_json(data: dict) -> BatchGetIncidentFindingsInput:
    out: BatchGetIncidentFindingsInput = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError("BatchGetIncidentFindingsInput.incident_record_arn required")
    if "findingIds" in data:
        import aws_sdk_ssm_incidents.types.finding_id_list
        out["finding_ids"] = aws_sdk_ssm_incidents.types.finding_id_list.deserialize_json(data["findingIds"])
    else:
        raise DeserializationError("BatchGetIncidentFindingsInput.finding_ids required")
    return out
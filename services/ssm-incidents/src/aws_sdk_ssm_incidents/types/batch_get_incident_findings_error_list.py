"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error

BatchGetIncidentFindingsErrorList: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.batch_get_incident_findings_error.BatchGetIncidentFindingsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsErrorList) -> list:
    import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_incidents.types.batch_get_incident_findings_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetIncidentFindingsErrorList:
    import aws_sdk_ssm_incidents.types.batch_get_incident_findings_error

    out: BatchGetIncidentFindingsErrorList = []
    for item in data:
        out.append(
            aws_sdk_ssm_incidents.types.batch_get_incident_findings_error.deserialize_json(
                item
            )
        )
    return out

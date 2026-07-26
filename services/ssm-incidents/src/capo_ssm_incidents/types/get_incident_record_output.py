"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetIncidentRecordOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.incident_record


class GetIncidentRecordOutput(TypedDict, closed=True):
    incident_record: "capo_ssm_incidents.types.incident_record.IncidentRecord"
    """<p>Details the structure of the incident record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIncidentRecordOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.incident_record

    out["incidentRecord"] = capo_ssm_incidents.types.incident_record.serialize_json(
        value["incident_record"]
    )
    return out


def deserialize_json(data: dict) -> GetIncidentRecordOutput:
    out: GetIncidentRecordOutput = {}  # type: ignore[typeddict-item]
    if "incidentRecord" in data:
        import capo_ssm_incidents.types.incident_record

        out["incident_record"] = (
            capo_ssm_incidents.types.incident_record.deserialize_json(
                data["incidentRecord"]
            )
        )
    else:
        raise DeserializationError("GetIncidentRecordOutput.incident_record required")
    return out

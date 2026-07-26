"""Generated from Smithy shape ``com.amazonaws.connecthealth#PatientInsightsEncounterContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.sensitive_non_empty_string


class PatientInsightsEncounterContext(TypedDict, closed=True):
    encounter_reason: (
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>Chief complaint for the visit</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatientInsightsEncounterContext) -> dict:
    out: dict = {}
    out["encounterReason"] = value["encounter_reason"]
    return out


def deserialize_json(data: dict) -> PatientInsightsEncounterContext:
    out: PatientInsightsEncounterContext = {}  # type: ignore[typeddict-item]
    if "encounterReason" in data:
        out["encounter_reason"] = data["encounterReason"]
    else:
        raise DeserializationError(
            "PatientInsightsEncounterContext.encounter_reason required"
        )
    return out

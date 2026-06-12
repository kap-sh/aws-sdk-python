"""Generated from Smithy shape ``com.amazonaws.bedrock#ValidityTerm``."""

from typing import TypedDict
from typing_extensions import NotRequired


class ValidityTerm(TypedDict):
    agreement_duration: NotRequired["str"]
    """<p>Describes the agreement duration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidityTerm) -> dict:
    out: dict = {}
    if "agreement_duration" in value:
        out["agreementDuration"] = value["agreement_duration"]
    return out


def deserialize_json(data: dict) -> ValidityTerm:
    out: ValidityTerm = {}  # type: ignore[typeddict-item]
    if "agreementDuration" in data:
        out["agreement_duration"] = data["agreementDuration"]
    return out

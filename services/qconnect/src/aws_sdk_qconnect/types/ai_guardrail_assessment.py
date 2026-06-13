"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailAssessment``."""

from typing import TypedDict

from aws_sdk_qconnect.errors import DeserializationError


class AIGuardrailAssessment(TypedDict):
    blocked: "bool"
    """<p>Indicates whether the AI Guardrail blocked the content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailAssessment) -> dict:
    out: dict = {}
    out["blocked"] = value["blocked"]
    return out


def deserialize_json(data: dict) -> AIGuardrailAssessment:
    out: AIGuardrailAssessment = {}  # type: ignore[typeddict-item]
    if "blocked" in data:
        out["blocked"] = data["blocked"]
    else:
        raise DeserializationError("AIGuardrailAssessment.blocked required")
    return out

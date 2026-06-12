"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailConfiguration``."""

from typing import TypedDict
from aws_sdk_bedrock.errors import DeserializationError


class GuardrailConfiguration(TypedDict):
    guardrail_id: "str"
    """<p>The unique identifier for the guardrail.</p>"""
    guardrail_version: "str"
    """<p>The version of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfiguration) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> GuardrailConfiguration:
    out: GuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if "guardrailId" in data:
        out["guardrail_id"] = data["guardrailId"]
    else:
        raise DeserializationError("GuardrailConfiguration.guardrail_id required")
    if "guardrailVersion" in data:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        raise DeserializationError("GuardrailConfiguration.guardrail_version required")
    return out

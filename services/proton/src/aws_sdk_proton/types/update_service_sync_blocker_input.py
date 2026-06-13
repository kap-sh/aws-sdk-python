"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceSyncBlockerInput``."""

from typing import TypedDict

from aws_sdk_proton.errors import DeserializationError


class UpdateServiceSyncBlockerInput(TypedDict):
    id: "str"
    """<p>The ID of the service sync blocker.</p>"""
    resolved_reason: "str"
    """<p>The reason the service sync blocker was resolved.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceSyncBlockerInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["resolvedReason"] = value["resolved_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceSyncBlockerInput:
    out: UpdateServiceSyncBlockerInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateServiceSyncBlockerInput.id required")
    if "resolvedReason" in data:
        out["resolved_reason"] = data["resolvedReason"]
    else:
        raise DeserializationError(
            "UpdateServiceSyncBlockerInput.resolved_reason required"
        )
    return out

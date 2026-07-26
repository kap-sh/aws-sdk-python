"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeReviewSettings``."""

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError


class CodeReviewSettings(TypedDict, closed=True):
    controls_scanning: "bool"
    """<p>Indicates whether controls scanning is enabled for code reviews.</p>"""
    general_purpose_scanning: "bool"
    """<p>Indicates whether general-purpose scanning is enabled for code reviews.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeReviewSettings) -> dict:
    out: dict = {}
    out["controlsScanning"] = value["controls_scanning"]
    out["generalPurposeScanning"] = value["general_purpose_scanning"]
    return out


def deserialize_json(data: dict) -> CodeReviewSettings:
    out: CodeReviewSettings = {}  # type: ignore[typeddict-item]
    if "controlsScanning" in data:
        out["controls_scanning"] = data["controlsScanning"]
    else:
        raise DeserializationError("CodeReviewSettings.controls_scanning required")
    if "generalPurposeScanning" in data:
        out["general_purpose_scanning"] = data["generalPurposeScanning"]
    else:
        raise DeserializationError(
            "CodeReviewSettings.general_purpose_scanning required"
        )
    return out

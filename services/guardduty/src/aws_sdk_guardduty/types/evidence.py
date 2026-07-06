"""Generated from Smithy shape ``com.amazonaws.guardduty#Evidence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.threat_intelligence_details


class Evidence(TypedDict, closed=True):
    threat_intelligence_details: NotRequired[
        "aws_sdk_guardduty.types.threat_intelligence_details.ThreatIntelligenceDetails"
    ]
    """<p>A list of threat intelligence details related to the evidence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evidence) -> dict:
    out: dict = {}
    if "threat_intelligence_details" in value:
        import aws_sdk_guardduty.types.threat_intelligence_details

        out["threatIntelligenceDetails"] = (
            aws_sdk_guardduty.types.threat_intelligence_details.serialize_json(
                value["threat_intelligence_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Evidence:
    out: Evidence = {}  # type: ignore[typeddict-item]
    if "threatIntelligenceDetails" in data:
        import aws_sdk_guardduty.types.threat_intelligence_details

        out["threat_intelligence_details"] = (
            aws_sdk_guardduty.types.threat_intelligence_details.deserialize_json(
                data["threatIntelligenceDetails"]
            )
        )
    return out

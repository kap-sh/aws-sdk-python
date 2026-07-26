"""Generated from Smithy shape ``com.amazonaws.guardduty#ThreatIntelligenceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.threat_names


class ThreatIntelligenceDetail(TypedDict, closed=True):
    threat_list_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the threat intelligence list that triggered the finding.</p>"""
    threat_names: NotRequired["capo_guardduty.types.threat_names.ThreatNames"]
    """<p>A list of names of the threats in the threat intelligence list that triggered the finding.</p>"""
    threat_file_sha256: NotRequired["capo_guardduty.types.string.String"]
    """<p>SHA256 of the file that generated the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThreatIntelligenceDetail) -> dict:
    out: dict = {}
    if "threat_list_name" in value:
        out["threatListName"] = value["threat_list_name"]
    if "threat_names" in value:
        import capo_guardduty.types.threat_names

        out["threatNames"] = capo_guardduty.types.threat_names.serialize_json(
            value["threat_names"]
        )
    if "threat_file_sha256" in value:
        out["threatFileSha256"] = value["threat_file_sha256"]
    return out


def deserialize_json(data: dict) -> ThreatIntelligenceDetail:
    out: ThreatIntelligenceDetail = {}  # type: ignore[typeddict-item]
    if "threatListName" in data:
        out["threat_list_name"] = data["threatListName"]
    if "threatNames" in data:
        import capo_guardduty.types.threat_names

        out["threat_names"] = capo_guardduty.types.threat_names.deserialize_json(
            data["threatNames"]
        )
    if "threatFileSha256" in data:
        out["threat_file_sha256"] = data["threatFileSha256"]
    return out

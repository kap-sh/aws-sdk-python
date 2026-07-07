"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingIdentifier``."""

from typing_extensions import TypedDict

from aws_sdk_codeguru_security.errors import DeserializationError


class FindingIdentifier(TypedDict, closed=True):
    scan_name: "str"
    """<p>The name of the scan that generated the finding. </p>"""
    finding_id: "str"
    """<p>The identifier for a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingIdentifier) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    out["findingId"] = value["finding_id"]
    return out


def deserialize_json(data: dict) -> FindingIdentifier:
    out: FindingIdentifier = {}  # type: ignore[typeddict-item]
    if "scanName" in data:
        out["scan_name"] = data["scanName"]
    else:
        raise DeserializationError("FindingIdentifier.scan_name required")
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError("FindingIdentifier.finding_id required")
    return out

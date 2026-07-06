"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseApex``."""

from typing_extensions import NotRequired, TypedDict


class AutonomousDatabaseApex(TypedDict, closed=True):
    apex_version: NotRequired["str"]
    """<p>The Oracle Application Express (APEX) version of the Autonomous Database.</p>"""
    ords_version: NotRequired["str"]
    """<p>The Oracle REST Data Services (ORDS) version of the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseApex) -> dict:
    out: dict = {}
    if "apex_version" in value:
        out["apexVersion"] = value["apex_version"]
    if "ords_version" in value:
        out["ordsVersion"] = value["ords_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseApex:
    out: AutonomousDatabaseApex = {}  # type: ignore[typeddict-item]
    if "apexVersion" in data:
        out["apex_version"] = data["apexVersion"]
    if "ordsVersion" in data:
        out["ords_version"] = data["ordsVersion"]
    return out

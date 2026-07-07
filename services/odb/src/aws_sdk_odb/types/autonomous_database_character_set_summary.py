"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseCharacterSetSummary``."""

from typing_extensions import NotRequired, TypedDict


class AutonomousDatabaseCharacterSetSummary(TypedDict, closed=True):
    character_set: NotRequired["str"]
    """<p>The name of the character set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseCharacterSetSummary) -> dict:
    out: dict = {}
    if "character_set" in value:
        out["characterSet"] = value["character_set"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseCharacterSetSummary:
    out: AutonomousDatabaseCharacterSetSummary = {}  # type: ignore[typeddict-item]
    if "characterSet" in data:
        out["character_set"] = data["characterSet"]
    return out

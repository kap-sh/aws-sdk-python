"""Generated from Smithy shape ``com.amazonaws.odb#GiVersionSummary``."""

from typing import TypedDict

from typing_extensions import NotRequired


class GiVersionSummary(TypedDict):
    version: NotRequired["str"]
    """<p>The GI software version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GiVersionSummary) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GiVersionSummary:
    out: GiVersionSummary = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    return out

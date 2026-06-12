"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#AccessDetails``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AccessDetails(TypedDict):
    description: NotRequired["str"]
    """<p>A description of the access privileges or permissions granted by this benefit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDetails) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDetails:
    out: AccessDetails = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.rekognition#Versions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.version


class Versions(TypedDict, closed=True):
    minimum: NotRequired["capo_rekognition.types.version.Version"]
    """<p>The desired minimum version for the challenge.</p>"""
    maximum: NotRequired["capo_rekognition.types.version.Version"]
    """<p>The desired maximum version for the challenge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Versions) -> dict:
    out: dict = {}
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Versions:
    out: Versions = {}  # type: ignore[typeddict-item]
    if "Minimum" in data:
        out["minimum"] = data["Minimum"]
    if "Maximum" in data:
        out["maximum"] = data["Maximum"]
    return out

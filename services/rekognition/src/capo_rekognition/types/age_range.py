"""Generated from Smithy shape ``com.amazonaws.rekognition#AgeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.u_integer


class AgeRange(TypedDict, closed=True):
    low: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>The lowest estimated age.</p>"""
    high: NotRequired["capo_rekognition.types.u_integer.UInteger"]
    """<p>The highest estimated age.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgeRange) -> dict:
    out: dict = {}
    if "low" in value:
        out["Low"] = value["low"]
    if "high" in value:
        out["High"] = value["high"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgeRange:
    out: AgeRange = {}  # type: ignore[typeddict-item]
    if "Low" in data:
        out["low"] = data["Low"]
    if "High" in data:
        out["high"] = data["High"]
    return out

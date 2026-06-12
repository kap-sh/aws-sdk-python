"""Generated from Smithy shape ``com.amazonaws.connect#Range``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.nullable_proficiency_level


class Range(TypedDict):
    min_proficiency_level: NotRequired[
        "aws_sdk_connect.types.nullable_proficiency_level.NullableProficiencyLevel"
    ]
    """<p>The minimum proficiency level of the range.</p>"""
    max_proficiency_level: NotRequired[
        "aws_sdk_connect.types.nullable_proficiency_level.NullableProficiencyLevel"
    ]
    """<p>The maximum proficiency level of the range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Range) -> dict:
    out: dict = {}
    if "min_proficiency_level" in value:
        out["MinProficiencyLevel"] = value["min_proficiency_level"]
    if "max_proficiency_level" in value:
        out["MaxProficiencyLevel"] = value["max_proficiency_level"]
    return out


def deserialize_json(data: dict) -> Range:
    out: Range = {}  # type: ignore[typeddict-item]
    if "MinProficiencyLevel" in data:
        out["min_proficiency_level"] = data["MinProficiencyLevel"]
    if "MaxProficiencyLevel" in data:
        out["max_proficiency_level"] = data["MaxProficiencyLevel"]
    return out

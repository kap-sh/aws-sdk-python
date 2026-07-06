"""Generated from Smithy shape ``com.amazonaws.macie2#SensitivityInspectionTemplatesEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class SensitivityInspectionTemplatesEntry(TypedDict, closed=True):
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the sensitivity inspection template.</p>"""
    name: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The name of the sensitivity inspection template: automated-sensitive-data-discovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SensitivityInspectionTemplatesEntry) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SensitivityInspectionTemplatesEntry:
    out: SensitivityInspectionTemplatesEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out

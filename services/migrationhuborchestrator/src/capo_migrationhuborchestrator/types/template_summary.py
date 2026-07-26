"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateSummary``."""

from typing_extensions import NotRequired, TypedDict


class TemplateSummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the template.</p>"""
    name: NotRequired["str"]
    """<p>The name of the template.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    description: NotRequired["str"]
    """<p>The description of the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "description" in data:
        out["description"] = data["description"]
    return out

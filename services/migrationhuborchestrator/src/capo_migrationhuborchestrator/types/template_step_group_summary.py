"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateStepGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.string_list


class TemplateStepGroupSummary(TypedDict, closed=True):
    id: NotRequired["str"]
    """<p>The ID of the step group.</p>"""
    name: NotRequired["str"]
    """<p>The name of the step group.</p>"""
    previous: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The previous step group.</p>"""
    next: NotRequired["capo_migrationhuborchestrator.types.string_list.StringList"]
    """<p>The next step group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateStepGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "previous" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.serialize_json(
                value["previous"]
            )
        )
    if "next" in value:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.serialize_json(
            value["next"]
        )
    return out


def deserialize_json(data: dict) -> TemplateStepGroupSummary:
    out: TemplateStepGroupSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "previous" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["previous"] = (
            capo_migrationhuborchestrator.types.string_list.deserialize_json(
                data["previous"]
            )
        )
    if "next" in data:
        import capo_migrationhuborchestrator.types.string_list

        out["next"] = capo_migrationhuborchestrator.types.string_list.deserialize_json(
            data["next"]
        )
    return out

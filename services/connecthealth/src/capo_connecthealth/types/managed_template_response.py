"""Generated from Smithy shape ``com.amazonaws.connecthealth#ManagedTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.managed_note_template


class ManagedTemplateResponse(TypedDict, closed=True):
    template_type: NotRequired[
        "capo_connecthealth.types.managed_note_template.ManagedNoteTemplate"
    ]
    """<p>The type of managed template used</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedTemplateResponse) -> dict:
    out: dict = {}
    if "template_type" in value:
        import capo_connecthealth.types.managed_note_template

        out["templateType"] = (
            capo_connecthealth.types.managed_note_template.serialize_json(
                value["template_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedTemplateResponse:
    out: ManagedTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import capo_connecthealth.types.managed_note_template

        out["template_type"] = (
            capo_connecthealth.types.managed_note_template.deserialize_json(
                data["templateType"]
            )
        )
    return out

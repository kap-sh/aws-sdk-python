"""Generated from Smithy shape ``com.amazonaws.connecthealth#ManagedTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.managed_note_template


class ManagedTemplateResponse(TypedDict):
    template_type: NotRequired[
        "aws_sdk_connecthealth.types.managed_note_template.ManagedNoteTemplate"
    ]
    """<p>The type of managed template used</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedTemplateResponse) -> dict:
    out: dict = {}
    if "template_type" in value:
        import aws_sdk_connecthealth.types.managed_note_template

        out["templateType"] = (
            aws_sdk_connecthealth.types.managed_note_template.serialize_json(
                value["template_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagedTemplateResponse:
    out: ManagedTemplateResponse = {}  # type: ignore[typeddict-item]
    if "templateType" in data:
        import aws_sdk_connecthealth.types.managed_note_template

        out["template_type"] = (
            aws_sdk_connecthealth.types.managed_note_template.deserialize_json(
                data["templateType"]
            )
        )
    return out

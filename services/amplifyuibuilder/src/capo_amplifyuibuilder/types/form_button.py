"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormButton``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.field_position


class FormButton(TypedDict, closed=True):
    excluded: NotRequired["bool"]
    """<p>Specifies whether the button is visible on the form.</p>"""
    children: NotRequired["str"]
    """<p>Describes the button's properties.</p>"""
    position: NotRequired["capo_amplifyuibuilder.types.field_position.FieldPosition"]
    """<p>The position of the button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormButton) -> dict:
    out: dict = {}
    if "excluded" in value:
        out["excluded"] = value["excluded"]
    if "children" in value:
        out["children"] = value["children"]
    if "position" in value:
        import capo_amplifyuibuilder.types.field_position

        out["position"] = capo_amplifyuibuilder.types.field_position.serialize_json(
            value["position"]
        )
    return out


def deserialize_json(data: dict) -> FormButton:
    out: FormButton = {}  # type: ignore[typeddict-item]
    if "excluded" in data:
        out["excluded"] = data["excluded"]
    if "children" in data:
        out["children"] = data["children"]
    if "position" in data:
        import capo_amplifyuibuilder.types.field_position

        out["position"] = capo_amplifyuibuilder.types.field_position.deserialize_json(
            data["position"]
        )
    return out

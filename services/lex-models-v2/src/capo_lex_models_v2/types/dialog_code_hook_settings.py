"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogCodeHookSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean


class DialogCodeHookSettings(TypedDict, closed=True):
    enabled: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Enables the dialog code hook so that it processes user requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DialogCodeHookSettings) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> DialogCodeHookSettings:
    out: DialogCodeHookSettings = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    return out

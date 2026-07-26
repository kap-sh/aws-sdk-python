"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MultipleValuesSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.boolean


class MultipleValuesSetting(TypedDict, closed=True):
    allow_multiple_values: "capo_lex_models_v2.types.boolean.Boolean"
    """<p>Indicates whether a slot can return multiple values. When <code>true</code>, the slot may return more than one value in a response. When <code>false</code>, the slot returns only a single value.</p> <p>Multi-value slots are only available in the en-US locale. If you set this value to <code>true</code> in any other locale, Amazon Lex throws a <code>ValidationException</code>.</p> <p>If the <code>allowMutlipleValues</code> is not set, the default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipleValuesSetting) -> dict:
    out: dict = {}
    out["allowMultipleValues"] = value.get("allow_multiple_values", False)
    return out


def deserialize_json(data: dict) -> MultipleValuesSetting:
    out: MultipleValuesSetting = {}  # type: ignore[typeddict-item]
    if "allowMultipleValues" in data:
        out["allow_multiple_values"] = data["allowMultipleValues"]
    else:
        out["allow_multiple_values"] = False
    return out

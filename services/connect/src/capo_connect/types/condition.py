"""Generated from Smithy shape ``com.amazonaws.connect#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.number_condition
    import capo_connect.types.string_condition


class Condition(TypedDict, closed=True):
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    """<p>A leaf node condition which can be used to specify a string condition.</p> <note> <p>The currently supported values for <code>FieldName</code> are <code>name</code> and <code>value</code>.</p> </note>"""
    number_condition: NotRequired["capo_connect.types.number_condition.NumberCondition"]
    """<p>A leaf node condition which can be used to specify a numeric condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    out: dict = {}
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "number_condition" in value:
        import capo_connect.types.number_condition

        out["NumberCondition"] = capo_connect.types.number_condition.serialize_json(
            value["number_condition"]
        )
    return out


def deserialize_json(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if "NumberCondition" in data:
        import capo_connect.types.number_condition

        out["number_condition"] = capo_connect.types.number_condition.deserialize_json(
            data["NumberCondition"]
        )
    return out

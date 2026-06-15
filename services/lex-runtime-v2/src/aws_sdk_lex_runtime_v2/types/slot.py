"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Slot``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.shape
    import aws_sdk_lex_runtime_v2.types.slots
    import aws_sdk_lex_runtime_v2.types.value
    import aws_sdk_lex_runtime_v2.types.values


class Slot(TypedDict):
    value: NotRequired["aws_sdk_lex_runtime_v2.types.value.Value"]
    """<p>The current value of the slot.</p>"""
    shape: NotRequired["aws_sdk_lex_runtime_v2.types.shape.Shape"]
    """<p>When the <code>shape</code> value is <code>List</code>, it indicates that the <code>values</code> field contains a list of slot values. When the value is <code>Scalar</code>, it indicates that the <code>value</code> field contains a single value.</p>"""
    values: NotRequired["aws_sdk_lex_runtime_v2.types.values.Values"]
    r"""<p>A list of one or more values that the user provided for the slot. For example, if a for a slot that elicits pizza toppings, the values might be \"pepperoni\" and \"pineapple.\" </p>"""
    sub_slots: NotRequired["aws_sdk_lex_runtime_v2.types.slots.Slots"]
    """<p>The constituent sub slots of a composite slot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Slot) -> dict:
    out: dict = {}
    if "value" in value:
        import aws_sdk_lex_runtime_v2.types.value

        out["value"] = aws_sdk_lex_runtime_v2.types.value.serialize_json(value["value"])
    if "shape" in value:
        import aws_sdk_lex_runtime_v2.types.shape

        out["shape"] = aws_sdk_lex_runtime_v2.types.shape.serialize_json(value["shape"])
    if "values" in value:
        import aws_sdk_lex_runtime_v2.types.values

        out["values"] = aws_sdk_lex_runtime_v2.types.values.serialize_json(
            value["values"]
        )
    if "sub_slots" in value:
        import aws_sdk_lex_runtime_v2.types.slots

        out["subSlots"] = aws_sdk_lex_runtime_v2.types.slots.serialize_json(
            value["sub_slots"]
        )
    return out


def deserialize_json(data: dict) -> Slot:
    out: Slot = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import aws_sdk_lex_runtime_v2.types.value

        out["value"] = aws_sdk_lex_runtime_v2.types.value.deserialize_json(
            data["value"]
        )
    if "shape" in data:
        import aws_sdk_lex_runtime_v2.types.shape

        out["shape"] = aws_sdk_lex_runtime_v2.types.shape.deserialize_json(
            data["shape"]
        )
    if "values" in data:
        import aws_sdk_lex_runtime_v2.types.values

        out["values"] = aws_sdk_lex_runtime_v2.types.values.deserialize_json(
            data["values"]
        )
    if "subSlots" in data:
        import aws_sdk_lex_runtime_v2.types.slots

        out["sub_slots"] = aws_sdk_lex_runtime_v2.types.slots.deserialize_json(
            data["subSlots"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotValueOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.slot_shape
    import aws_sdk_lex_models_v2.types.slot_value
    import aws_sdk_lex_models_v2.types.slot_values


class SlotValueOverride(TypedDict):
    shape: NotRequired["aws_sdk_lex_models_v2.types.slot_shape.SlotShape"]
    """<p>When the shape value is <code>List</code>, it indicates that the <code>values</code> field contains a list of slot values. When the value is <code>Scalar</code>, it indicates that the <code>value</code> field contains a single value.</p>"""
    value: NotRequired["aws_sdk_lex_models_v2.types.slot_value.SlotValue"]
    """<p>The current value of the slot.</p>"""
    values: NotRequired["aws_sdk_lex_models_v2.types.slot_values.SlotValues"]
    r"""<p>A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be \"pepperoni\" and \"pineapple.\"</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotValueOverride) -> dict:
    out: dict = {}
    if "shape" in value:
        import aws_sdk_lex_models_v2.types.slot_shape

        out["shape"] = aws_sdk_lex_models_v2.types.slot_shape.serialize_json(
            value["shape"]
        )
    if "value" in value:
        import aws_sdk_lex_models_v2.types.slot_value

        out["value"] = aws_sdk_lex_models_v2.types.slot_value.serialize_json(
            value["value"]
        )
    if "values" in value:
        import aws_sdk_lex_models_v2.types.slot_values

        out["values"] = aws_sdk_lex_models_v2.types.slot_values.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SlotValueOverride:
    out: SlotValueOverride = {}  # type: ignore[typeddict-item]
    if "shape" in data:
        import aws_sdk_lex_models_v2.types.slot_shape

        out["shape"] = aws_sdk_lex_models_v2.types.slot_shape.deserialize_json(
            data["shape"]
        )
    if "value" in data:
        import aws_sdk_lex_models_v2.types.slot_value

        out["value"] = aws_sdk_lex_models_v2.types.slot_value.deserialize_json(
            data["value"]
        )
    if "values" in data:
        import aws_sdk_lex_models_v2.types.slot_values

        out["values"] = aws_sdk_lex_models_v2.types.slot_values.deserialize_json(
            data["values"]
        )
    return out

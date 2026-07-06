"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#SlotFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.filter_values
    import aws_sdk_lex_models_v2.types.slot_filter_name
    import aws_sdk_lex_models_v2.types.slot_filter_operator


class SlotFilter(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.slot_filter_name.SlotFilterName"
    """<p>The name of the field to use for filtering.</p>"""
    values: "aws_sdk_lex_models_v2.types.filter_values.FilterValues"
    """<p>The value to use to filter the response.</p>"""
    operator: "aws_sdk_lex_models_v2.types.slot_filter_operator.SlotFilterOperator"
    """<p>The operator to use for the filter. Specify <code>EQ</code> when the <code>ListSlots</code> operation should return only aliases that equal the specified value. Specify <code>CO</code> when the <code>ListSlots</code> operation should return aliases that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlotFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.slot_filter_name

    out["name"] = aws_sdk_lex_models_v2.types.slot_filter_name.serialize_json(
        value["name"]
    )
    import aws_sdk_lex_models_v2.types.filter_values

    out["values"] = aws_sdk_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import aws_sdk_lex_models_v2.types.slot_filter_operator

    out["operator"] = aws_sdk_lex_models_v2.types.slot_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> SlotFilter:
    out: SlotFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.slot_filter_name

        out["name"] = aws_sdk_lex_models_v2.types.slot_filter_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("SlotFilter.name required")
    if "values" in data:
        import aws_sdk_lex_models_v2.types.filter_values

        out["values"] = aws_sdk_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SlotFilter.values required")
    if "operator" in data:
        import aws_sdk_lex_models_v2.types.slot_filter_operator

        out["operator"] = (
            aws_sdk_lex_models_v2.types.slot_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("SlotFilter.operator required")
    return out

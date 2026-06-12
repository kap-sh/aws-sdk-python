"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentFilter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.filter_values
    import aws_sdk_lex_models_v2.types.intent_filter_name
    import aws_sdk_lex_models_v2.types.intent_filter_operator


class IntentFilter(TypedDict):
    name: "aws_sdk_lex_models_v2.types.intent_filter_name.IntentFilterName"
    """<p>The name of the field to use for the filter.</p>"""
    values: "aws_sdk_lex_models_v2.types.filter_values.FilterValues"
    """<p>The value to use for the filter.</p>"""
    operator: "aws_sdk_lex_models_v2.types.intent_filter_operator.IntentFilterOperator"
    """<p>The operator to use for the filter. Specify <code>EQ</code> when the <code>ListIntents</code> operation should return only aliases that equal the specified value. Specify <code>CO</code> when the <code>ListIntents</code> operation should return aliases that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.intent_filter_name

    out["name"] = aws_sdk_lex_models_v2.types.intent_filter_name.serialize_json(
        value["name"]
    )
    import aws_sdk_lex_models_v2.types.filter_values

    out["values"] = aws_sdk_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import aws_sdk_lex_models_v2.types.intent_filter_operator

    out["operator"] = aws_sdk_lex_models_v2.types.intent_filter_operator.serialize_json(
        value["operator"]
    )
    return out


def deserialize_json(data: dict) -> IntentFilter:
    out: IntentFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.intent_filter_name

        out["name"] = aws_sdk_lex_models_v2.types.intent_filter_name.deserialize_json(
            data["name"]
        )
    else:
        raise DeserializationError("IntentFilter.name required")
    if "values" in data:
        import aws_sdk_lex_models_v2.types.filter_values

        out["values"] = aws_sdk_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("IntentFilter.values required")
    if "operator" in data:
        import aws_sdk_lex_models_v2.types.intent_filter_operator

        out["operator"] = (
            aws_sdk_lex_models_v2.types.intent_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("IntentFilter.operator required")
    return out

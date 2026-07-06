"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_filter_name
    import aws_sdk_lex_models_v2.types.bot_locale_filter_operator
    import aws_sdk_lex_models_v2.types.filter_values


class BotLocaleFilter(TypedDict, closed=True):
    name: "aws_sdk_lex_models_v2.types.bot_locale_filter_name.BotLocaleFilterName"
    """<p>The name of the field to filter the list of bots.</p>"""
    values: "aws_sdk_lex_models_v2.types.filter_values.FilterValues"
    """<p>The value to use for filtering the list of bots.</p>"""
    operator: (
        "aws_sdk_lex_models_v2.types.bot_locale_filter_operator.BotLocaleFilterOperator"
    )
    """<p>The operator to use for the filter. Specify <code>EQ</code> when the <code>ListBotLocales</code> operation should return only aliases that equal the specified value. Specify <code>CO</code> when the <code>ListBotLocales</code> operation should return aliases that contain the specified value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleFilter) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.bot_locale_filter_name

    out["name"] = aws_sdk_lex_models_v2.types.bot_locale_filter_name.serialize_json(
        value["name"]
    )
    import aws_sdk_lex_models_v2.types.filter_values

    out["values"] = aws_sdk_lex_models_v2.types.filter_values.serialize_json(
        value["values"]
    )
    import aws_sdk_lex_models_v2.types.bot_locale_filter_operator

    out["operator"] = (
        aws_sdk_lex_models_v2.types.bot_locale_filter_operator.serialize_json(
            value["operator"]
        )
    )
    return out


def deserialize_json(data: dict) -> BotLocaleFilter:
    out: BotLocaleFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_filter_name

        out["name"] = (
            aws_sdk_lex_models_v2.types.bot_locale_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("BotLocaleFilter.name required")
    if "values" in data:
        import aws_sdk_lex_models_v2.types.filter_values

        out["values"] = aws_sdk_lex_models_v2.types.filter_values.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("BotLocaleFilter.values required")
    if "operator" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_filter_operator

        out["operator"] = (
            aws_sdk_lex_models_v2.types.bot_locale_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("BotLocaleFilter.operator required")
    return out

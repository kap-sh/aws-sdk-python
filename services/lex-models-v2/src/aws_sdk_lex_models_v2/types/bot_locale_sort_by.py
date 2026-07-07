"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotLocaleSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.bot_locale_sort_attribute
    import aws_sdk_lex_models_v2.types.sort_order


class BotLocaleSortBy(TypedDict, closed=True):
    attribute: (
        "aws_sdk_lex_models_v2.types.bot_locale_sort_attribute.BotLocaleSortAttribute"
    )
    """<p>The bot locale attribute to sort by.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>Specifies whether to sort the bot locales in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotLocaleSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.bot_locale_sort_attribute

    out["attribute"] = (
        aws_sdk_lex_models_v2.types.bot_locale_sort_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> BotLocaleSortBy:
    out: BotLocaleSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.bot_locale_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.bot_locale_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("BotLocaleSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("BotLocaleSortBy.order required")
    return out

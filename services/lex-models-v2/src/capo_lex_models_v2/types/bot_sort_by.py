"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_sort_attribute
    import capo_lex_models_v2.types.sort_order


class BotSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.bot_sort_attribute.BotSortAttribute"
    """<p>The attribute to use to sort the list of bots.</p>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list. You can choose ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.bot_sort_attribute

    out["attribute"] = capo_lex_models_v2.types.bot_sort_attribute.serialize_json(
        value["attribute"]
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> BotSortBy:
    out: BotSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import capo_lex_models_v2.types.bot_sort_attribute

        out["attribute"] = capo_lex_models_v2.types.bot_sort_attribute.deserialize_json(
            data["attribute"]
        )
    else:
        raise DeserializationError("BotSortBy.attribute required")
    if "order" in data:
        import capo_lex_models_v2.types.sort_order

        out["order"] = capo_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("BotSortBy.order required")
    return out

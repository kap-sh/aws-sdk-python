"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImportSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.import_sort_attribute
    import capo_lex_models_v2.types.sort_order


class ImportSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.import_sort_attribute.ImportSortAttribute"
    """<p>The export field to use for sorting.</p>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.import_sort_attribute

    out["attribute"] = capo_lex_models_v2.types.import_sort_attribute.serialize_json(
        value["attribute"]
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> ImportSortBy:
    out: ImportSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import capo_lex_models_v2.types.import_sort_attribute

        out["attribute"] = (
            capo_lex_models_v2.types.import_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("ImportSortBy.attribute required")
    if "order" in data:
        import capo_lex_models_v2.types.sort_order

        out["order"] = capo_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("ImportSortBy.order required")
    return out

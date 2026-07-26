"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.sort_order
    import capo_lex_models_v2.types.test_set_sort_attribute


class TestSetSortBy(TypedDict, closed=True):
    attribute: "capo_lex_models_v2.types.test_set_sort_attribute.TestSetSortAttribute"
    """<p>Specifies whether to sort the test sets by name or by the time they were last updated.</p>"""
    order: "capo_lex_models_v2.types.sort_order.SortOrder"
    """<p>Specifies whether to sort in ascending or descending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetSortBy) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.test_set_sort_attribute

    out["attribute"] = capo_lex_models_v2.types.test_set_sort_attribute.serialize_json(
        value["attribute"]
    )
    import capo_lex_models_v2.types.sort_order

    out["order"] = capo_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> TestSetSortBy:
    out: TestSetSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import capo_lex_models_v2.types.test_set_sort_attribute

        out["attribute"] = (
            capo_lex_models_v2.types.test_set_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("TestSetSortBy.attribute required")
    if "order" in data:
        import capo_lex_models_v2.types.sort_order

        out["order"] = capo_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("TestSetSortBy.order required")
    return out

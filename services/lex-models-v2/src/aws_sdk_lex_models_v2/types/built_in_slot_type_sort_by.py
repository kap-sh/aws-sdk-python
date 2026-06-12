"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuiltInSlotTypeSortBy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute
    import aws_sdk_lex_models_v2.types.sort_order


class BuiltInSlotTypeSortBy(TypedDict):
    attribute: "aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute.BuiltInSlotTypeSortAttribute"
    """<p>The attribute to use to sort the list of built-in intents.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list. You can choose ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuiltInSlotTypeSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute

    out["attribute"] = (
        aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> BuiltInSlotTypeSortBy:
    out: BuiltInSlotTypeSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.built_in_slot_type_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("BuiltInSlotTypeSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("BuiltInSlotTypeSortBy.order required")
    return out

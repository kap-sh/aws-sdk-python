"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#IntentSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.intent_sort_attribute
    import aws_sdk_lex_models_v2.types.sort_order


class IntentSortBy(TypedDict, closed=True):
    attribute: "aws_sdk_lex_models_v2.types.intent_sort_attribute.IntentSortAttribute"
    """<p>The attribute to use to sort the list of intents.</p>"""
    order: "aws_sdk_lex_models_v2.types.sort_order.SortOrder"
    """<p>The order to sort the list. You can choose ascending or descending.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentSortBy) -> dict:
    out: dict = {}
    import aws_sdk_lex_models_v2.types.intent_sort_attribute

    out["attribute"] = aws_sdk_lex_models_v2.types.intent_sort_attribute.serialize_json(
        value["attribute"]
    )
    import aws_sdk_lex_models_v2.types.sort_order

    out["order"] = aws_sdk_lex_models_v2.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> IntentSortBy:
    out: IntentSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_lex_models_v2.types.intent_sort_attribute

        out["attribute"] = (
            aws_sdk_lex_models_v2.types.intent_sort_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("IntentSortBy.attribute required")
    if "order" in data:
        import aws_sdk_lex_models_v2.types.sort_order

        out["order"] = aws_sdk_lex_models_v2.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("IntentSortBy.order required")
    return out

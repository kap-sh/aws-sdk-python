"""Generated from Smithy shape ``com.amazonaws.bedrock#RatingScaleItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.rating_scale_item_definition
    import capo_bedrock.types.rating_scale_item_value


class RatingScaleItem(TypedDict, closed=True):
    definition: (
        "capo_bedrock.types.rating_scale_item_definition.RatingScaleItemDefinition"
    )
    """<p>Defines the definition for one rating in a custom metric rating scale.</p>"""
    value: "capo_bedrock.types.rating_scale_item_value.RatingScaleItemValue"
    """<p>Defines the value for one rating in a custom metric rating scale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RatingScaleItem) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    import capo_bedrock.types.rating_scale_item_value

    out["value"] = capo_bedrock.types.rating_scale_item_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> RatingScaleItem:
    out: RatingScaleItem = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("RatingScaleItem.definition required")
    if "value" in data:
        import capo_bedrock.types.rating_scale_item_value

        out["value"] = capo_bedrock.types.rating_scale_item_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("RatingScaleItem.value required")
    return out

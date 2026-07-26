"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ItemIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.item_type
    import capo_ssm_incidents.types.item_value


class ItemIdentifier(TypedDict, closed=True):
    value: "capo_ssm_incidents.types.item_value.ItemValue"
    """<p>Details about the related item.</p>"""
    type: "capo_ssm_incidents.types.item_type.ItemType"
    """<p>The type of related item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemIdentifier) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.item_value

    out["value"] = capo_ssm_incidents.types.item_value.serialize_json(value["value"])
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ItemIdentifier:
    out: ItemIdentifier = {}  # type: ignore[typeddict-item]
    if "value" in data:
        import capo_ssm_incidents.types.item_value

        out["value"] = capo_ssm_incidents.types.item_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("ItemIdentifier.value required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("ItemIdentifier.type required")
    return out

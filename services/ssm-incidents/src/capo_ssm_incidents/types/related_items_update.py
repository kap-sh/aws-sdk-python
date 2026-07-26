"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RelatedItemsUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.item_identifier
    import capo_ssm_incidents.types.related_item


class _RelatedItemsUpdate_itemToAdd(TypedDict, closed=True):
    itemToAdd: "capo_ssm_incidents.types.related_item.RelatedItem"


class _RelatedItemsUpdate_itemToRemove(TypedDict, closed=True):
    itemToRemove: "capo_ssm_incidents.types.item_identifier.ItemIdentifier"


RelatedItemsUpdate: TypeAlias = (
    _RelatedItemsUpdate_itemToAdd | _RelatedItemsUpdate_itemToRemove
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemsUpdate) -> dict:
    if "itemToAdd" in value:
        import capo_ssm_incidents.types.related_item

        return {
            "itemToAdd": capo_ssm_incidents.types.related_item.serialize_json(
                value["itemToAdd"]
            )
        }
    elif "itemToRemove" in value:
        import capo_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": capo_ssm_incidents.types.item_identifier.serialize_json(
                value["itemToRemove"]
            )
        }
    else:
        raise SerializationError("RelatedItemsUpdate: no variant present")


def deserialize_json(data: dict) -> RelatedItemsUpdate:
    if "itemToAdd" in data:
        import capo_ssm_incidents.types.related_item

        return {
            "itemToAdd": capo_ssm_incidents.types.related_item.deserialize_json(
                data["itemToAdd"]
            )
        }
    elif "itemToRemove" in data:
        import capo_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": capo_ssm_incidents.types.item_identifier.deserialize_json(
                data["itemToRemove"]
            )
        }
    else:
        raise DeserializationError("RelatedItemsUpdate: no recognized variant key")

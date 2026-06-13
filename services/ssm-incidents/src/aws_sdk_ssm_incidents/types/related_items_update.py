"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RelatedItemsUpdate``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.item_identifier
    import aws_sdk_ssm_incidents.types.related_item


class _RelatedItemsUpdate_itemToAdd(TypedDict):
    itemToAdd: "aws_sdk_ssm_incidents.types.related_item.RelatedItem"


class _RelatedItemsUpdate_itemToRemove(TypedDict):
    itemToRemove: "aws_sdk_ssm_incidents.types.item_identifier.ItemIdentifier"


RelatedItemsUpdate: TypeAlias = (
    _RelatedItemsUpdate_itemToAdd | _RelatedItemsUpdate_itemToRemove
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemsUpdate) -> dict:
    if "itemToAdd" in value:
        import aws_sdk_ssm_incidents.types.related_item

        return {
            "itemToAdd": aws_sdk_ssm_incidents.types.related_item.serialize_json(
                value["itemToAdd"]
            )
        }
    elif "itemToRemove" in value:
        import aws_sdk_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": aws_sdk_ssm_incidents.types.item_identifier.serialize_json(
                value["itemToRemove"]
            )
        }
    else:
        raise SerializationError("RelatedItemsUpdate: no variant present")


def deserialize_json(data: dict) -> RelatedItemsUpdate:
    if "itemToAdd" in data:
        import aws_sdk_ssm_incidents.types.related_item

        return {
            "itemToAdd": aws_sdk_ssm_incidents.types.related_item.deserialize_json(
                data["itemToAdd"]
            )
        }
    elif "itemToRemove" in data:
        import aws_sdk_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": aws_sdk_ssm_incidents.types.item_identifier.deserialize_json(
                data["itemToRemove"]
            )
        }
    else:
        raise DeserializationError("RelatedItemsUpdate: no recognized variant key")

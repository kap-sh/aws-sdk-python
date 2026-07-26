"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInventoryResultItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_item
    import capo_datazone.types.data_product_result_item
    import capo_datazone.types.glossary_item
    import capo_datazone.types.glossary_term_item


class _SearchInventoryResultItem_glossaryItem(TypedDict, closed=True):
    glossaryItem: "capo_datazone.types.glossary_item.GlossaryItem"


class _SearchInventoryResultItem_glossaryTermItem(TypedDict, closed=True):
    glossaryTermItem: "capo_datazone.types.glossary_term_item.GlossaryTermItem"


class _SearchInventoryResultItem_assetItem(TypedDict, closed=True):
    assetItem: "capo_datazone.types.asset_item.AssetItem"


class _SearchInventoryResultItem_dataProductItem(TypedDict, closed=True):
    dataProductItem: (
        "capo_datazone.types.data_product_result_item.DataProductResultItem"
    )


SearchInventoryResultItem: TypeAlias = (
    _SearchInventoryResultItem_glossaryItem
    | _SearchInventoryResultItem_glossaryTermItem
    | _SearchInventoryResultItem_assetItem
    | _SearchInventoryResultItem_dataProductItem
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchInventoryResultItem) -> dict:
    if "glossaryItem" in value:
        import capo_datazone.types.glossary_item

        return {
            "glossaryItem": capo_datazone.types.glossary_item.serialize_json(
                value["glossaryItem"]
            )
        }
    elif "glossaryTermItem" in value:
        import capo_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": capo_datazone.types.glossary_term_item.serialize_json(
                value["glossaryTermItem"]
            )
        }
    elif "assetItem" in value:
        import capo_datazone.types.asset_item

        return {
            "assetItem": capo_datazone.types.asset_item.serialize_json(
                value["assetItem"]
            )
        }
    elif "dataProductItem" in value:
        import capo_datazone.types.data_product_result_item

        return {
            "dataProductItem": capo_datazone.types.data_product_result_item.serialize_json(
                value["dataProductItem"]
            )
        }
    else:
        raise SerializationError("SearchInventoryResultItem: no variant present")


def deserialize_json(data: dict) -> SearchInventoryResultItem:
    if "glossaryItem" in data:
        import capo_datazone.types.glossary_item

        return {
            "glossaryItem": capo_datazone.types.glossary_item.deserialize_json(
                data["glossaryItem"]
            )
        }
    elif "glossaryTermItem" in data:
        import capo_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": capo_datazone.types.glossary_term_item.deserialize_json(
                data["glossaryTermItem"]
            )
        }
    elif "assetItem" in data:
        import capo_datazone.types.asset_item

        return {
            "assetItem": capo_datazone.types.asset_item.deserialize_json(
                data["assetItem"]
            )
        }
    elif "dataProductItem" in data:
        import capo_datazone.types.data_product_result_item

        return {
            "dataProductItem": capo_datazone.types.data_product_result_item.deserialize_json(
                data["dataProductItem"]
            )
        }
    else:
        raise DeserializationError(
            "SearchInventoryResultItem: no recognized variant key"
        )

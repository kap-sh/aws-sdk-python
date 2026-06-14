"""Generated from Smithy shape ``com.amazonaws.datazone#SearchInventoryResultItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_item
    import aws_sdk_datazone.types.data_product_result_item
    import aws_sdk_datazone.types.glossary_item
    import aws_sdk_datazone.types.glossary_term_item


class _SearchInventoryResultItem_glossaryItem(TypedDict):
    glossaryItem: "aws_sdk_datazone.types.glossary_item.GlossaryItem"


class _SearchInventoryResultItem_glossaryTermItem(TypedDict):
    glossaryTermItem: "aws_sdk_datazone.types.glossary_term_item.GlossaryTermItem"


class _SearchInventoryResultItem_assetItem(TypedDict):
    assetItem: "aws_sdk_datazone.types.asset_item.AssetItem"


class _SearchInventoryResultItem_dataProductItem(TypedDict):
    dataProductItem: (
        "aws_sdk_datazone.types.data_product_result_item.DataProductResultItem"
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
        import aws_sdk_datazone.types.glossary_item

        return {
            "glossaryItem": aws_sdk_datazone.types.glossary_item.serialize_json(
                value["glossaryItem"]
            )
        }
    elif "glossaryTermItem" in value:
        import aws_sdk_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": aws_sdk_datazone.types.glossary_term_item.serialize_json(
                value["glossaryTermItem"]
            )
        }
    elif "assetItem" in value:
        import aws_sdk_datazone.types.asset_item

        return {
            "assetItem": aws_sdk_datazone.types.asset_item.serialize_json(
                value["assetItem"]
            )
        }
    elif "dataProductItem" in value:
        import aws_sdk_datazone.types.data_product_result_item

        return {
            "dataProductItem": aws_sdk_datazone.types.data_product_result_item.serialize_json(
                value["dataProductItem"]
            )
        }
    else:
        raise SerializationError("SearchInventoryResultItem: no variant present")


def deserialize_json(data: dict) -> SearchInventoryResultItem:
    if "glossaryItem" in data:
        import aws_sdk_datazone.types.glossary_item

        return {
            "glossaryItem": aws_sdk_datazone.types.glossary_item.deserialize_json(
                data["glossaryItem"]
            )
        }
    elif "glossaryTermItem" in data:
        import aws_sdk_datazone.types.glossary_term_item

        return {
            "glossaryTermItem": aws_sdk_datazone.types.glossary_term_item.deserialize_json(
                data["glossaryTermItem"]
            )
        }
    elif "assetItem" in data:
        import aws_sdk_datazone.types.asset_item

        return {
            "assetItem": aws_sdk_datazone.types.asset_item.deserialize_json(
                data["assetItem"]
            )
        }
    elif "dataProductItem" in data:
        import aws_sdk_datazone.types.data_product_result_item

        return {
            "dataProductItem": aws_sdk_datazone.types.data_product_result_item.deserialize_json(
                data["dataProductItem"]
            )
        }
    else:
        raise DeserializationError(
            "SearchInventoryResultItem: no recognized variant key"
        )

"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesResultItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.asset_type_item
    import capo_datazone.types.form_type_data
    import capo_datazone.types.lineage_node_type_item


class _SearchTypesResultItem_assetTypeItem(TypedDict, closed=True):
    assetTypeItem: "capo_datazone.types.asset_type_item.AssetTypeItem"


class _SearchTypesResultItem_formTypeItem(TypedDict, closed=True):
    formTypeItem: "capo_datazone.types.form_type_data.FormTypeData"


class _SearchTypesResultItem_lineageNodeTypeItem(TypedDict, closed=True):
    lineageNodeTypeItem: (
        "capo_datazone.types.lineage_node_type_item.LineageNodeTypeItem"
    )


SearchTypesResultItem: TypeAlias = (
    _SearchTypesResultItem_assetTypeItem
    | _SearchTypesResultItem_formTypeItem
    | _SearchTypesResultItem_lineageNodeTypeItem
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesResultItem) -> dict:
    if "assetTypeItem" in value:
        import capo_datazone.types.asset_type_item

        return {
            "assetTypeItem": capo_datazone.types.asset_type_item.serialize_json(
                value["assetTypeItem"]
            )
        }
    elif "formTypeItem" in value:
        import capo_datazone.types.form_type_data

        return {
            "formTypeItem": capo_datazone.types.form_type_data.serialize_json(
                value["formTypeItem"]
            )
        }
    elif "lineageNodeTypeItem" in value:
        import capo_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": capo_datazone.types.lineage_node_type_item.serialize_json(
                value["lineageNodeTypeItem"]
            )
        }
    else:
        raise SerializationError("SearchTypesResultItem: no variant present")


def deserialize_json(data: dict) -> SearchTypesResultItem:
    if "assetTypeItem" in data:
        import capo_datazone.types.asset_type_item

        return {
            "assetTypeItem": capo_datazone.types.asset_type_item.deserialize_json(
                data["assetTypeItem"]
            )
        }
    elif "formTypeItem" in data:
        import capo_datazone.types.form_type_data

        return {
            "formTypeItem": capo_datazone.types.form_type_data.deserialize_json(
                data["formTypeItem"]
            )
        }
    elif "lineageNodeTypeItem" in data:
        import capo_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": capo_datazone.types.lineage_node_type_item.deserialize_json(
                data["lineageNodeTypeItem"]
            )
        }
    else:
        raise DeserializationError("SearchTypesResultItem: no recognized variant key")

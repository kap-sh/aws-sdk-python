"""Generated from Smithy shape ``com.amazonaws.datazone#SearchTypesResultItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_type_item
    import aws_sdk_datazone.types.form_type_data
    import aws_sdk_datazone.types.lineage_node_type_item


class _SearchTypesResultItem_assetTypeItem(TypedDict):
    assetTypeItem: "aws_sdk_datazone.types.asset_type_item.AssetTypeItem"


class _SearchTypesResultItem_formTypeItem(TypedDict):
    formTypeItem: "aws_sdk_datazone.types.form_type_data.FormTypeData"


class _SearchTypesResultItem_lineageNodeTypeItem(TypedDict):
    lineageNodeTypeItem: (
        "aws_sdk_datazone.types.lineage_node_type_item.LineageNodeTypeItem"
    )


SearchTypesResultItem: TypeAlias = (
    _SearchTypesResultItem_assetTypeItem
    | _SearchTypesResultItem_formTypeItem
    | _SearchTypesResultItem_lineageNodeTypeItem
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchTypesResultItem) -> dict:
    if "assetTypeItem" in value:
        import aws_sdk_datazone.types.asset_type_item

        return {
            "assetTypeItem": aws_sdk_datazone.types.asset_type_item.serialize_json(
                value["assetTypeItem"]
            )
        }
    elif "formTypeItem" in value:
        import aws_sdk_datazone.types.form_type_data

        return {
            "formTypeItem": aws_sdk_datazone.types.form_type_data.serialize_json(
                value["formTypeItem"]
            )
        }
    elif "lineageNodeTypeItem" in value:
        import aws_sdk_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": aws_sdk_datazone.types.lineage_node_type_item.serialize_json(
                value["lineageNodeTypeItem"]
            )
        }
    else:
        raise SerializationError("SearchTypesResultItem: no variant present")


def deserialize_json(data: dict) -> SearchTypesResultItem:
    if "assetTypeItem" in data:
        import aws_sdk_datazone.types.asset_type_item

        return {
            "assetTypeItem": aws_sdk_datazone.types.asset_type_item.deserialize_json(
                data["assetTypeItem"]
            )
        }
    elif "formTypeItem" in data:
        import aws_sdk_datazone.types.form_type_data

        return {
            "formTypeItem": aws_sdk_datazone.types.form_type_data.deserialize_json(
                data["formTypeItem"]
            )
        }
    elif "lineageNodeTypeItem" in data:
        import aws_sdk_datazone.types.lineage_node_type_item

        return {
            "lineageNodeTypeItem": aws_sdk_datazone.types.lineage_node_type_item.deserialize_json(
                data["lineageNodeTypeItem"]
            )
        }
    else:
        raise DeserializationError("SearchTypesResultItem: no recognized variant key")

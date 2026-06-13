"""Generated from Smithy shape ``com.amazonaws.datazone#ResultItem``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_node_item


class _ResultItem_lineageNode(TypedDict):
    lineageNode: "aws_sdk_datazone.types.lineage_node_item.LineageNodeItem"


ResultItem: TypeAlias = _ResultItem_lineageNode


# --- restJson1 ser/de ---
def serialize_json(value: ResultItem) -> dict:
    if "lineageNode" in value:
        import aws_sdk_datazone.types.lineage_node_item

        return {
            "lineageNode": aws_sdk_datazone.types.lineage_node_item.serialize_json(
                value["lineageNode"]
            )
        }
    else:
        raise SerializationError("ResultItem: no variant present")


def deserialize_json(data: dict) -> ResultItem:
    if "lineageNode" in data:
        import aws_sdk_datazone.types.lineage_node_item

        return {
            "lineageNode": aws_sdk_datazone.types.lineage_node_item.deserialize_json(
                data["lineageNode"]
            )
        }
    else:
        raise DeserializationError("ResultItem: no recognized variant key")

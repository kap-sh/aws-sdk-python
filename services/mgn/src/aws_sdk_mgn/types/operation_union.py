"""Generated from Smithy shape ``com.amazonaws.mgn#OperationUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mgn.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.delete_operation
    import aws_sdk_mgn.types.merge_operation
    import aws_sdk_mgn.types.split_operation
    import aws_sdk_mgn.types.update_operation


class _OperationUnion_merge(TypedDict, closed=True):
    merge: "aws_sdk_mgn.types.merge_operation.MergeOperation"


class _OperationUnion_split(TypedDict, closed=True):
    split: "aws_sdk_mgn.types.split_operation.SplitOperation"


class _OperationUnion_delete(TypedDict, closed=True):
    delete: "aws_sdk_mgn.types.delete_operation.DeleteOperation"


class _OperationUnion_update(TypedDict, closed=True):
    update: "aws_sdk_mgn.types.update_operation.UpdateOperation"


OperationUnion: TypeAlias = (
    _OperationUnion_merge
    | _OperationUnion_split
    | _OperationUnion_delete
    | _OperationUnion_update
)


# --- restJson1 ser/de ---
def serialize_json(value: OperationUnion) -> dict:
    if "merge" in value:
        import aws_sdk_mgn.types.merge_operation

        return {
            "merge": aws_sdk_mgn.types.merge_operation.serialize_json(value["merge"])
        }
    elif "split" in value:
        import aws_sdk_mgn.types.split_operation

        return {
            "split": aws_sdk_mgn.types.split_operation.serialize_json(value["split"])
        }
    elif "delete" in value:
        import aws_sdk_mgn.types.delete_operation

        return {
            "delete": aws_sdk_mgn.types.delete_operation.serialize_json(value["delete"])
        }
    elif "update" in value:
        import aws_sdk_mgn.types.update_operation

        return {
            "update": aws_sdk_mgn.types.update_operation.serialize_json(value["update"])
        }
    else:
        raise SerializationError("OperationUnion: no variant present")


def deserialize_json(data: dict) -> OperationUnion:
    if "merge" in data:
        import aws_sdk_mgn.types.merge_operation

        return {
            "merge": aws_sdk_mgn.types.merge_operation.deserialize_json(data["merge"])
        }
    elif "split" in data:
        import aws_sdk_mgn.types.split_operation

        return {
            "split": aws_sdk_mgn.types.split_operation.deserialize_json(data["split"])
        }
    elif "delete" in data:
        import aws_sdk_mgn.types.delete_operation

        return {
            "delete": aws_sdk_mgn.types.delete_operation.deserialize_json(
                data["delete"]
            )
        }
    elif "update" in data:
        import aws_sdk_mgn.types.update_operation

        return {
            "update": aws_sdk_mgn.types.update_operation.deserialize_json(
                data["update"]
            )
        }
    else:
        raise DeserializationError("OperationUnion: no recognized variant key")

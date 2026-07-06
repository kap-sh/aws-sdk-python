"""Generated from Smithy shape ``com.amazonaws.entityresolution#BatchDeleteUniqueIdOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.delete_unique_id_errors_list
    import aws_sdk_entityresolution.types.delete_unique_id_status
    import aws_sdk_entityresolution.types.deleted_unique_id_list
    import aws_sdk_entityresolution.types.disconnected_unique_ids_list


class BatchDeleteUniqueIdOutput(TypedDict, closed=True):
    status: (
        "aws_sdk_entityresolution.types.delete_unique_id_status.DeleteUniqueIdStatus"
    )
    """<p>The status of the batch delete unique ID operation.</p>"""
    errors: "aws_sdk_entityresolution.types.delete_unique_id_errors_list.DeleteUniqueIdErrorsList"
    """<p> The errors from deleting multiple unique IDs.</p>"""
    deleted: "aws_sdk_entityresolution.types.deleted_unique_id_list.DeletedUniqueIdList"
    """<p>The unique IDs that were deleted.</p>"""
    disconnected_unique_ids: "aws_sdk_entityresolution.types.disconnected_unique_ids_list.DisconnectedUniqueIdsList"
    """<p>The unique IDs that were disconnected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUniqueIdOutput) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.delete_unique_id_status

    out["status"] = (
        aws_sdk_entityresolution.types.delete_unique_id_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_entityresolution.types.delete_unique_id_errors_list

    out["errors"] = (
        aws_sdk_entityresolution.types.delete_unique_id_errors_list.serialize_json(
            value["errors"]
        )
    )
    import aws_sdk_entityresolution.types.deleted_unique_id_list

    out["deleted"] = (
        aws_sdk_entityresolution.types.deleted_unique_id_list.serialize_json(
            value["deleted"]
        )
    )
    import aws_sdk_entityresolution.types.disconnected_unique_ids_list

    out["disconnectedUniqueIds"] = (
        aws_sdk_entityresolution.types.disconnected_unique_ids_list.serialize_json(
            value["disconnected_unique_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteUniqueIdOutput:
    out: BatchDeleteUniqueIdOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_entityresolution.types.delete_unique_id_status

        out["status"] = (
            aws_sdk_entityresolution.types.delete_unique_id_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteUniqueIdOutput.status required")
    if "errors" in data:
        import aws_sdk_entityresolution.types.delete_unique_id_errors_list

        out["errors"] = (
            aws_sdk_entityresolution.types.delete_unique_id_errors_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteUniqueIdOutput.errors required")
    if "deleted" in data:
        import aws_sdk_entityresolution.types.deleted_unique_id_list

        out["deleted"] = (
            aws_sdk_entityresolution.types.deleted_unique_id_list.deserialize_json(
                data["deleted"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteUniqueIdOutput.deleted required")
    if "disconnectedUniqueIds" in data:
        import aws_sdk_entityresolution.types.disconnected_unique_ids_list

        out["disconnected_unique_ids"] = (
            aws_sdk_entityresolution.types.disconnected_unique_ids_list.deserialize_json(
                data["disconnectedUniqueIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteUniqueIdOutput.disconnected_unique_ids required"
        )
    return out

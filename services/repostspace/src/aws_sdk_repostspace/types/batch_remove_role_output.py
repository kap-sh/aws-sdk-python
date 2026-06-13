"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveRoleOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.batch_error_list


class BatchRemoveRoleOutput(TypedDict):
    removed_accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>An array of successfully updated accessor identifiers.</p>"""
    errors: "aws_sdk_repostspace.types.batch_error_list.BatchErrorList"
    """<p>An array of errors that occurred when roles were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveRoleOutput) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.accessor_id_list

    out["removedAccessorIds"] = (
        aws_sdk_repostspace.types.accessor_id_list.serialize_json(
            value["removed_accessor_ids"]
        )
    )
    import aws_sdk_repostspace.types.batch_error_list

    out["errors"] = aws_sdk_repostspace.types.batch_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchRemoveRoleOutput:
    out: BatchRemoveRoleOutput = {}  # type: ignore[typeddict-item]
    if "removedAccessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list

        out["removed_accessor_ids"] = (
            aws_sdk_repostspace.types.accessor_id_list.deserialize_json(
                data["removedAccessorIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchRemoveRoleOutput.removed_accessor_ids required"
        )
    if "errors" in data:
        import aws_sdk_repostspace.types.batch_error_list

        out["errors"] = aws_sdk_repostspace.types.batch_error_list.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("BatchRemoveRoleOutput.errors required")
    return out

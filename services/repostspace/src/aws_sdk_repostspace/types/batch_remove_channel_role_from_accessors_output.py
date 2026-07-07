"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveChannelRoleFromAccessorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.batch_error_list


class BatchRemoveChannelRoleFromAccessorsOutput(TypedDict, closed=True):
    removed_accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>An array of successfully updated identifiers.</p>"""
    errors: "aws_sdk_repostspace.types.batch_error_list.BatchErrorList"
    """<p>An array of errors that occurred when roles were removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveChannelRoleFromAccessorsOutput) -> dict:
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


def deserialize_json(data: dict) -> BatchRemoveChannelRoleFromAccessorsOutput:
    out: BatchRemoveChannelRoleFromAccessorsOutput = {}  # type: ignore[typeddict-item]
    if "removedAccessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list

        out["removed_accessor_ids"] = (
            aws_sdk_repostspace.types.accessor_id_list.deserialize_json(
                data["removedAccessorIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchRemoveChannelRoleFromAccessorsOutput.removed_accessor_ids required"
        )
    if "errors" in data:
        import aws_sdk_repostspace.types.batch_error_list

        out["errors"] = aws_sdk_repostspace.types.batch_error_list.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError(
            "BatchRemoveChannelRoleFromAccessorsOutput.errors required"
        )
    return out

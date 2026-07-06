"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchAddChannelRoleToAccessorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.batch_error_list


class BatchAddChannelRoleToAccessorsOutput(TypedDict, closed=True):
    added_accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>An array of successfully updated identifiers.</p>"""
    errors: "aws_sdk_repostspace.types.batch_error_list.BatchErrorList"
    """<p>An array of errors that occurred when roles were added.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchAddChannelRoleToAccessorsOutput) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.accessor_id_list

    out["addedAccessorIds"] = aws_sdk_repostspace.types.accessor_id_list.serialize_json(
        value["added_accessor_ids"]
    )
    import aws_sdk_repostspace.types.batch_error_list

    out["errors"] = aws_sdk_repostspace.types.batch_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> BatchAddChannelRoleToAccessorsOutput:
    out: BatchAddChannelRoleToAccessorsOutput = {}  # type: ignore[typeddict-item]
    if "addedAccessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list

        out["added_accessor_ids"] = (
            aws_sdk_repostspace.types.accessor_id_list.deserialize_json(
                data["addedAccessorIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAddChannelRoleToAccessorsOutput.added_accessor_ids required"
        )
    if "errors" in data:
        import aws_sdk_repostspace.types.batch_error_list

        out["errors"] = aws_sdk_repostspace.types.batch_error_list.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError(
            "BatchAddChannelRoleToAccessorsOutput.errors required"
        )
    return out

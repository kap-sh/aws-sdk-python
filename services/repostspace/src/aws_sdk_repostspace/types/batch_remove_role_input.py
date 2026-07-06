"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchRemoveRoleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.role
    import aws_sdk_repostspace.types.space_id


class BatchRemoveRoleInput(TypedDict, closed=True):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The user or group accessor identifiers to remove the role from.</p>"""
    role: "aws_sdk_repostspace.types.role.Role"
    """<p>The role to remove from the users or groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchRemoveRoleInput) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.accessor_id_list

    out["accessorIds"] = aws_sdk_repostspace.types.accessor_id_list.serialize_json(
        value["accessor_ids"]
    )
    import aws_sdk_repostspace.types.role

    out["role"] = aws_sdk_repostspace.types.role.serialize_json(value["role"])
    return out


def deserialize_json(data: dict) -> BatchRemoveRoleInput:
    out: BatchRemoveRoleInput = {}  # type: ignore[typeddict-item]
    if "accessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list

        out["accessor_ids"] = (
            aws_sdk_repostspace.types.accessor_id_list.deserialize_json(
                data["accessorIds"]
            )
        )
    else:
        raise DeserializationError("BatchRemoveRoleInput.accessor_ids required")
    if "role" in data:
        import aws_sdk_repostspace.types.role

        out["role"] = aws_sdk_repostspace.types.role.deserialize_json(data["role"])
    else:
        raise DeserializationError("BatchRemoveRoleInput.role required")
    return out

"""Generated from Smithy shape ``com.amazonaws.repostspace#Roles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id
    import aws_sdk_repostspace.types.role_list

Roles: TypeAlias = dict[
    "aws_sdk_repostspace.types.accessor_id.AccessorId",
    "aws_sdk_repostspace.types.role_list.RoleList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Roles) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_repostspace.types.role_list

        out[key] = aws_sdk_repostspace.types.role_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> Roles:
    out: Roles = {}
    for key, value in data.items():
        import aws_sdk_repostspace.types.role_list

        out[key] = aws_sdk_repostspace.types.role_list.deserialize_json(value)
    return out

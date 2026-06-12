"""Generated from Smithy shape ``com.amazonaws.opensearch#InstanceRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.instance_role

InstanceRoleList: TypeAlias = list[
    "aws_sdk_opensearch.types.instance_role.InstanceRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceRoleList) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceRoleList:
    return list(data)

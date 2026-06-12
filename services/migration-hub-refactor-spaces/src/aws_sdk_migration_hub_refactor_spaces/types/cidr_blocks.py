"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CidrBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.cidr_block

CidrBlocks: TypeAlias = list[
    "aws_sdk_migration_hub_refactor_spaces.types.cidr_block.CidrBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: CidrBlocks) -> list:
    return list(value)


def deserialize_json(data: list) -> CidrBlocks:
    return list(data)

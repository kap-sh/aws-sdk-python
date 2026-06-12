"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#HttpMethods``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.http_method

HttpMethods: TypeAlias = list[
    "aws_sdk_migration_hub_refactor_spaces.types.http_method.HttpMethod"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpMethods) -> list:
    return list(value)


def deserialize_json(data: list) -> HttpMethods:
    return list(data)

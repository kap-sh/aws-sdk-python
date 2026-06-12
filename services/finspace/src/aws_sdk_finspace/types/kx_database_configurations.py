"""Generated from Smithy shape ``com.amazonaws.finspace#KxDatabaseConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.kx_database_configuration

KxDatabaseConfigurations: TypeAlias = list[
    "aws_sdk_finspace.types.kx_database_configuration.KxDatabaseConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: KxDatabaseConfigurations) -> list:
    import aws_sdk_finspace.types.kx_database_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_finspace.types.kx_database_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KxDatabaseConfigurations:
    import aws_sdk_finspace.types.kx_database_configuration

    out: KxDatabaseConfigurations = []
    for item in data:
        out.append(
            aws_sdk_finspace.types.kx_database_configuration.deserialize_json(item)
        )
    return out

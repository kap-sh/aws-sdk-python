"""Generated from Smithy shape ``com.amazonaws.aiops#CrossAccountConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_aiops.types.cross_account_configuration

CrossAccountConfigurations: TypeAlias = list[
    "aws_sdk_aiops.types.cross_account_configuration.CrossAccountConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountConfigurations) -> list:
    import aws_sdk_aiops.types.cross_account_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_aiops.types.cross_account_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CrossAccountConfigurations:
    import aws_sdk_aiops.types.cross_account_configuration

    out: CrossAccountConfigurations = []
    for item in data:
        out.append(
            aws_sdk_aiops.types.cross_account_configuration.deserialize_json(item)
        )
    return out

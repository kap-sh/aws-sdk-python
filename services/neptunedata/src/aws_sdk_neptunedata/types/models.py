"""Generated from Smithy shape ``com.amazonaws.neptunedata#Models``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.ml_config_definition

Models: TypeAlias = list[
    "aws_sdk_neptunedata.types.ml_config_definition.MlConfigDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: Models) -> list:
    import aws_sdk_neptunedata.types.ml_config_definition

    out: list = []
    for item in value:
        out.append(aws_sdk_neptunedata.types.ml_config_definition.serialize_json(item))
    return out


def deserialize_json(data: list) -> Models:
    import aws_sdk_neptunedata.types.ml_config_definition

    out: Models = []
    for item in data:
        out.append(
            aws_sdk_neptunedata.types.ml_config_definition.deserialize_json(item)
        )
    return out

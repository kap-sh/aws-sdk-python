"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceInputSourceConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.id_namespace_input_source

IdNamespaceInputSourceConfig: TypeAlias = list[
    "aws_sdk_entityresolution.types.id_namespace_input_source.IdNamespaceInputSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceInputSourceConfig) -> list:
    import aws_sdk_entityresolution.types.id_namespace_input_source

    out: list = []
    for item in value:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_input_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> IdNamespaceInputSourceConfig:
    import aws_sdk_entityresolution.types.id_namespace_input_source

    out: IdNamespaceInputSourceConfig = []
    for item in data:
        out.append(
            aws_sdk_entityresolution.types.id_namespace_input_source.deserialize_json(
                item
            )
        )
    return out

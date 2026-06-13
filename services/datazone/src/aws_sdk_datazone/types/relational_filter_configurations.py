"""Generated from Smithy shape ``com.amazonaws.datazone#RelationalFilterConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.relational_filter_configuration

RelationalFilterConfigurations: TypeAlias = list[
    "aws_sdk_datazone.types.relational_filter_configuration.RelationalFilterConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelationalFilterConfigurations) -> list:
    import aws_sdk_datazone.types.relational_filter_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.relational_filter_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RelationalFilterConfigurations:
    import aws_sdk_datazone.types.relational_filter_configuration

    out: RelationalFilterConfigurations = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.relational_filter_configuration.deserialize_json(
                item
            )
        )
    return out

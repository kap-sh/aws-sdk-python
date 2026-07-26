"""Generated from Smithy shape ``com.amazonaws.databrew#ValidationConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_databrew.types.validation_configuration

ValidationConfigurationList: TypeAlias = list[
    "capo_databrew.types.validation_configuration.ValidationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationConfigurationList) -> list:
    import capo_databrew.types.validation_configuration

    out: list = []
    for item in value:
        out.append(capo_databrew.types.validation_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationConfigurationList:
    import capo_databrew.types.validation_configuration

    out: ValidationConfigurationList = []
    for item in data:
        out.append(capo_databrew.types.validation_configuration.deserialize_json(item))
    return out

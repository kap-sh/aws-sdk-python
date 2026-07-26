"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfParameterDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.parameter_definition

__listOfParameterDefinition: TypeAlias = list[
    "capo_serverlessapplicationrepository.types.parameter_definition.ParameterDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfParameterDefinition) -> list:
    import capo_serverlessapplicationrepository.types.parameter_definition

    out: list = []
    for item in value:
        out.append(
            capo_serverlessapplicationrepository.types.parameter_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfParameterDefinition:
    import capo_serverlessapplicationrepository.types.parameter_definition

    out: __listOfParameterDefinition = []
    for item in data:
        out.append(
            capo_serverlessapplicationrepository.types.parameter_definition.deserialize_json(
                item
            )
        )
    return out

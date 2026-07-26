"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.parameter_value

__listOfParameterValue: TypeAlias = list[
    "capo_serverlessapplicationrepository.types.parameter_value.ParameterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfParameterValue) -> list:
    import capo_serverlessapplicationrepository.types.parameter_value

    out: list = []
    for item in value:
        out.append(
            capo_serverlessapplicationrepository.types.parameter_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfParameterValue:
    import capo_serverlessapplicationrepository.types.parameter_value

    out: __listOfParameterValue = []
    for item in data:
        out.append(
            capo_serverlessapplicationrepository.types.parameter_value.deserialize_json(
                item
            )
        )
    return out

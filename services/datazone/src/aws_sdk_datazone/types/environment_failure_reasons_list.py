"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentFailureReasonsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_error

EnvironmentFailureReasonsList: TypeAlias = list[
    "aws_sdk_datazone.types.environment_error.EnvironmentError"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentFailureReasonsList) -> list:
    import aws_sdk_datazone.types.environment_error

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.environment_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentFailureReasonsList:
    import aws_sdk_datazone.types.environment_error

    out: EnvironmentFailureReasonsList = []
    for item in data:
        out.append(aws_sdk_datazone.types.environment_error.deserialize_json(item))
    return out

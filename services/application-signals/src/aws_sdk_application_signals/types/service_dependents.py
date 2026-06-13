"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceDependents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_dependent

ServiceDependents: TypeAlias = list[
    "aws_sdk_application_signals.types.service_dependent.ServiceDependent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDependents) -> list:
    import aws_sdk_application_signals.types.service_dependent

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_dependent.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceDependents:
    import aws_sdk_application_signals.types.service_dependent

    out: ServiceDependents = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_dependent.deserialize_json(item)
        )
    return out

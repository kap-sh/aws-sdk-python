"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceDependencies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_dependency

ServiceDependencies: TypeAlias = list[
    "aws_sdk_application_signals.types.service_dependency.ServiceDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceDependencies) -> list:
    import aws_sdk_application_signals.types.service_dependency

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_dependency.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceDependencies:
    import aws_sdk_application_signals.types.service_dependency

    out: ServiceDependencies = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_dependency.deserialize_json(item)
        )
    return out

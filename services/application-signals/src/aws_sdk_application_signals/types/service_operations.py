"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_operation

ServiceOperations: TypeAlias = list[
    "aws_sdk_application_signals.types.service_operation.ServiceOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceOperations) -> list:
    import aws_sdk_application_signals.types.service_operation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_signals.types.service_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceOperations:
    import aws_sdk_application_signals.types.service_operation

    out: ServiceOperations = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_operation.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceStates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_state

ServiceStates: TypeAlias = list[
    "aws_sdk_application_signals.types.service_state.ServiceState"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceStates) -> list:
    import aws_sdk_application_signals.types.service_state

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.service_state.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceStates:
    import aws_sdk_application_signals.types.service_state

    out: ServiceStates = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_state.deserialize_json(item)
        )
    return out

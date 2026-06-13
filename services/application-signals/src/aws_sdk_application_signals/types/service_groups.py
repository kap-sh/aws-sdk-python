"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_group

ServiceGroups: TypeAlias = list[
    "aws_sdk_application_signals.types.service_group.ServiceGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceGroups) -> list:
    import aws_sdk_application_signals.types.service_group

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.service_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceGroups:
    import aws_sdk_application_signals.types.service_group

    out: ServiceGroups = []
    for item in data:
        out.append(
            aws_sdk_application_signals.types.service_group.deserialize_json(item)
        )
    return out

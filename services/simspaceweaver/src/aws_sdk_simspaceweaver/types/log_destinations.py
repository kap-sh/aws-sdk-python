"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LogDestinations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_simspaceweaver.types.log_destination

LogDestinations: TypeAlias = list[
    "aws_sdk_simspaceweaver.types.log_destination.LogDestination"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogDestinations) -> list:
    import aws_sdk_simspaceweaver.types.log_destination

    out: list = []
    for item in value:
        out.append(aws_sdk_simspaceweaver.types.log_destination.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogDestinations:
    import aws_sdk_simspaceweaver.types.log_destination

    out: LogDestinations = []
    for item in data:
        out.append(aws_sdk_simspaceweaver.types.log_destination.deserialize_json(item))
    return out

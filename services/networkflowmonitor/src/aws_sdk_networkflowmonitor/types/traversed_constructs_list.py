"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#TraversedConstructsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.traversed_component

TraversedConstructsList: TypeAlias = list[
    "aws_sdk_networkflowmonitor.types.traversed_component.TraversedComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: TraversedConstructsList) -> list:
    import aws_sdk_networkflowmonitor.types.traversed_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkflowmonitor.types.traversed_component.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TraversedConstructsList:
    import aws_sdk_networkflowmonitor.types.traversed_component

    out: TraversedConstructsList = []
    for item in data:
        out.append(
            aws_sdk_networkflowmonitor.types.traversed_component.deserialize_json(item)
        )
    return out

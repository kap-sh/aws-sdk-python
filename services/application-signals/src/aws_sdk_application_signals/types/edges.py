"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Edges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.edge

Edges: TypeAlias = list["aws_sdk_application_signals.types.edge.Edge"]


# --- restJson1 ser/de ---
def serialize_json(value: Edges) -> list:
    import aws_sdk_application_signals.types.edge

    out: list = []
    for item in value:
        out.append(aws_sdk_application_signals.types.edge.serialize_json(item))
    return out


def deserialize_json(data: list) -> Edges:
    import aws_sdk_application_signals.types.edge

    out: Edges = []
    for item in data:
        out.append(aws_sdk_application_signals.types.edge.deserialize_json(item))
    return out
